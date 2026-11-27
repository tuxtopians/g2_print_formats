// Copyright (c) 2026, Savad Ibrahim and Contributors
// License: MIT
//
// Default mapped report Print Formats to G2 styles.
// Report DocType has no default_print_format field; the print dialog Link is blank
// unless we set it here.

(function () {
	frappe.provide("g2_print_formats.report_print");

	const DEFAULTS = {
		"General Ledger": "G2 Party Ledger",
		"Accounts Receivable Report": "G2 Outstanding Invoices",
		"Accounts Payable Report": "G2 Outstanding Payables",
		"Accounts Receivable": "G2 Customer Outstanding",
	};

	function current_report_name() {
		return (frappe.query_report && frappe.query_report.report_name) || "";
	}

	function default_for_current_report() {
		return DEFAULTS[current_report_name()] || null;
	}

	function apply_default(dialog, print_format_name) {
		if (!print_format_name || !dialog || !dialog.fields_dict) {
			return;
		}
		const field = dialog.fields_dict.print_format;
		if (!field) {
			return;
		}
		// Avoid Link validate clearing the value before the control is ready
		field.df.ignore_link_validation = 1;
		field.df.default = print_format_name;
		field.set_value(print_format_name);
	}

	function install() {
		if (frappe.ui._g2_report_print_settings_patched) {
			// Keep DEFAULTS reference current if script reloads
			g2_print_formats.report_print.DEFAULTS = DEFAULTS;
			return;
		}
		const original = frappe.ui.get_print_settings;
		if (typeof original !== "function") {
			return;
		}

		frappe.ui.get_print_settings = function (
			pdf,
			callback,
			letter_head,
			pick_columns,
			has_filters,
			title
		) {
			const print_format_name = default_for_current_report();
			const _prompt = frappe.prompt;

			// Inject field default before Dialog is built (most reliable)
			if (print_format_name) {
				frappe.prompt = function (fields, cb, t, primary_label) {
					const next = (fields || []).map(function (f) {
						if (f && f.fieldname === "print_format") {
							return Object.assign({}, f, { default: print_format_name });
						}
						return f;
					});
					frappe.prompt = _prompt;
					return _prompt(next, cb, t, primary_label);
				};
			}

			let dialog;
			try {
				dialog = original(
					pdf,
					callback,
					letter_head,
					pick_columns,
					has_filters,
					title
				);
			} finally {
				frappe.prompt = _prompt;
			}

			apply_default(dialog, print_format_name);
			// Link controls sometimes need a tick after show()
			if (print_format_name && dialog) {
				setTimeout(function () {
					apply_default(dialog, print_format_name);
				}, 0);
			}
			return dialog;
		};

		frappe.ui._g2_report_print_settings_patched = true;
	}

	g2_print_formats.report_print.install = install;
	g2_print_formats.report_print.DEFAULTS = DEFAULTS;

	$(document).on("app_ready", install);
	if (frappe.boot) {
		install();
	}
})();
