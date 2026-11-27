// Switch default print format by document Finance Book.
// FZBook -> G2 FZ *; otherwise -> G2 * (Property Setter fallback).

(function () {
	const FZ_FINANCE_BOOK = "FZBook";

	const DOCTYPE_FORMAT_SUFFIX = {
		"Purchase Order": "Purchase Order",
		"Sales Invoice": "Sales Invoice",
		Quotation: "Quotation",
		"Sales Order": "Sales Order",
		"Delivery Note": "Delivery Note",
		"Purchase Invoice": "Purchase Invoice",
		"Purchase Receipt": "Purchase Receipt",
		"Payment Entry": "Payment Voucher",
		"Expense Entry": "Expense Entry",
		"Proforma Invoice": "Proforma Invoice",
		"Consolidated Proforma Invoice": "Consolidated Proforma Invoice",
		"Journal Entry": "Journal Entry",
	};

	function get_preferred_print_format(frm) {
		if (!frm || !frm.doctype || !frm.doc) {
			return null;
		}

		const suffix = DOCTYPE_FORMAT_SUFFIX[frm.doctype];
		if (!suffix) {
			return null;
		}

		const use_fz = frm.doc.finance_book === FZ_FINANCE_BOOK;
		return (use_fz ? "G2 FZ " : "G2 ") + suffix;
	}

	function wrap_print_view(Cls) {
		if (!Cls || !Cls.prototype || Cls.prototype._g2_fb_print_patched) {
			return Cls;
		}

		const original = Cls.prototype.set_default_print_format;
		Cls.prototype.set_default_print_format = function () {
			const preferred = get_preferred_print_format(this.frm);
			const formats = frappe.meta.get_print_formats(this.frm.doctype);

			if (preferred && formats.includes(preferred)) {
				this.print_format_selector.empty();
				this.print_format_selector.val(preferred);
				return;
			}

			return original.call(this);
		};

		Cls.prototype._g2_fb_print_patched = true;
		return Cls;
	}

	frappe.provide("frappe.ui.form");

	let stored_print_view = frappe.ui.form.PrintView || null;
	if (stored_print_view) {
		stored_print_view = wrap_print_view(stored_print_view);
	}

	Object.defineProperty(frappe.ui.form, "PrintView", {
		configurable: true,
		enumerable: true,
		get() {
			return stored_print_view;
		},
		set(Cls) {
			stored_print_view = wrap_print_view(Cls);
		},
	});
})();
