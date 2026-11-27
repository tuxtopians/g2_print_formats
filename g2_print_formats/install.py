from __future__ import annotations

import json
import os

APP_NAME = "g2_print_formats"
MODULE = "G2 Print Formats"
TEMPLATE_DIR = "templates/print_formats"

# Stable timestamps keep exported JSON diffs focused on content, not metadata.
STABLE_GIT_TIMESTAMP = "2000-01-01 00:00:00.000000"
GIT_TIMESTAMP_FIELDS = ("creation", "modified")

TEMPLATE_PARTIALS = (
	"g2_decorations.html",
	"g2_doc_number_vars.html",
	"g2_header_company.html",
	"g2_header_plain.html",
	"g2_document_meta.html",
	"g2_party_address.html",
	"g2_items_footer.html",
	"g2_items_footer_fz.html",
	"g2_delivery_note_items_footer.html",
	"g2_fz_delivery_note_items_footer.html",
	"g2_purchase_receipt_items_footer.html",
	"g2_fz_purchase_receipt_items_footer.html",
	"g2_purchase_order_items_footer.html",
	"g2_fz_purchase_order_items_footer.html",
	"g2_expense_items_footer.html",
	"g2_expense_items_footer_fz.html",
	"g2_proforma_items_footer.html",
	"g2_proforma_party.html",
	"g2_approval_signatures.html",
)

PRINT_FORMATS: tuple[dict[str, str], ...] = (
	{
		"name": "G2 Purchase Order",
		"doc_type": "Purchase Order",
		"html_file": "g2_purchase_order.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Sales Invoice",
		"doc_type": "Sales Invoice",
		"html_file": "g2_sales_invoice.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Quotation",
		"doc_type": "Quotation",
		"html_file": "g2_quotation.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Sales Order",
		"doc_type": "Sales Order",
		"html_file": "g2_sales_order.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Delivery Note",
		"doc_type": "Delivery Note",
		"html_file": "g2_delivery_note.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Purchase Invoice",
		"doc_type": "Purchase Invoice",
		"html_file": "g2_purchase_invoice.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Purchase Receipt",
		"doc_type": "Purchase Receipt",
		"html_file": "g2_purchase_receipt.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Payment Voucher",
		"doc_type": "Payment Entry",
		"html_file": "g2_payment_voucher.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Payment Voucher Bulk",
		"doc_type": "Payment Voucher",
		"html_file": "g2_payment_voucher_bulk.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Expense Entry",
		"doc_type": "Expense Entry",
		"html_file": "g2_expense_entry.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Payment Request",
		"doc_type": "Payment Request",
		"html_file": "g2_payment_request.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Proforma Invoice",
		"doc_type": "Proforma Invoice",
		"html_file": "g2_proforma_invoice.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Quote",
		"doc_type": "Quote",
		"html_file": "g2_proforma_invoice.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Consolidated Proforma Invoice",
		"doc_type": "Consolidated Proforma Invoice",
		"html_file": "g2_consolidated_proforma_invoice.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Journal Entry",
		"doc_type": "Journal Entry",
		"html_file": "g2_journal_entry.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 Pay Slip",
		"doc_type": "Salary Slip",
		"html_file": "g2_pay_slip.html",
		"css_file": "g2_styles.css",
	},
	{
		"name": "G2 FZ Purchase Order",
		"doc_type": "Purchase Order",
		"html_file": "g2_fz_purchase_order.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Sales Invoice",
		"doc_type": "Sales Invoice",
		"html_file": "g2_fz_sales_invoice.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Quotation",
		"doc_type": "Quotation",
		"html_file": "g2_fz_quotation.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Sales Order",
		"doc_type": "Sales Order",
		"html_file": "g2_fz_sales_order.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Delivery Note",
		"doc_type": "Delivery Note",
		"html_file": "g2_fz_delivery_note.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Purchase Invoice",
		"doc_type": "Purchase Invoice",
		"html_file": "g2_fz_purchase_invoice.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Purchase Receipt",
		"doc_type": "Purchase Receipt",
		"html_file": "g2_fz_purchase_receipt.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Payment Voucher",
		"doc_type": "Payment Entry",
		"html_file": "g2_fz_payment_voucher.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Payment Voucher Bulk",
		"doc_type": "Payment Voucher",
		"html_file": "g2_fz_payment_voucher_bulk.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Expense Entry",
		"doc_type": "Expense Entry",
		"html_file": "g2_fz_expense_entry.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Payment Request",
		"doc_type": "Payment Request",
		"html_file": "g2_fz_payment_request.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Proforma Invoice",
		"doc_type": "Proforma Invoice",
		"html_file": "g2_fz_proforma_invoice.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Quote",
		"doc_type": "Quote",
		"html_file": "g2_fz_proforma_invoice.html",
		"css_file": "g2_styles_fz.css",
	},
	{
		"name": "G2 FZ Consolidated Proforma Invoice",
		"doc_type": "Consolidated Proforma Invoice",
		"html_file": "g2_fz_consolidated_proforma_invoice.html",
		"css_file": "g2_styles_fz.css",
		"finance_book": "FZBook",
	},
	{
		"name": "G2 FZ Journal Entry",
		"doc_type": "Journal Entry",
		"html_file": "g2_fz_journal_entry.html",
		"css_file": "g2_styles_fz.css",
		"finance_book": "FZBook",
	},
)

# Report print formats (JS templates rendered by Query Report print)
REPORT_PRINT_FORMATS: tuple[dict[str, str], ...] = (
	{
		"name": "G2 Monthly Profit and Loss",
		"report": "Profit and Loss Statement",
		"html_file": "g2_monthly_pnl.html",
	},
	{
		"name": "G2 Balance Sheet",
		"report": "Balance Sheet",
		"html_file": "g2_balance_sheet.html",
	},
	{
		"name": "G2 Party Ledger",
		"report": "General Ledger",
		"html_file": "g2_party_ledger.html",
	},
	{
		"name": "G2 Outstanding Invoices",
		"report": "Accounts Receivable Report",
		"html_file": "g2_outstanding_invoices.html",
	},
	{
		"name": "G2 Outstanding Payables",
		"report": "Accounts Payable Report",
		"html_file": "g2_outstanding_payables.html",
	},
	{
		"name": "G2 Customer Outstanding",
		"report": "Accounts Receivable",
		"html_file": "g2_customer_outstanding.html",
	},
)

# Report print formats registered in REPORT_PRINT_FORMATS.
# Note: Report DocType has no default_print_format DB field; desk print dialog
# is defaulted via public/js/general_ledger_print_format.js for mapped reports.
DEFAULT_REPORT_PRINT_FORMATS: dict[str, str] = {
	"General Ledger": "G2 Party Ledger",
	"Accounts Receivable Report": "G2 Outstanding Invoices",
	"Accounts Payable Report": "G2 Outstanding Payables",
	"Accounts Receivable": "G2 Customer Outstanding",
}

# Legacy "G2 Black *" names renamed to "G2 FZ *"
LEGACY_PRINT_FORMAT_RENAMES: dict[str, str] = {
	"G2 Black Purchase Order": "G2 FZ Purchase Order",
	"G2 Black Sales Invoice": "G2 FZ Sales Invoice",
	"G2 Black Quotation": "G2 FZ Quotation",
	"G2 Black Sales Order": "G2 FZ Sales Order",
	"G2 Black Delivery Note": "G2 FZ Delivery Note",
	"G2 Black Purchase Invoice": "G2 FZ Purchase Invoice",
	"G2 Black Purchase Receipt": "G2 FZ Purchase Receipt",
	"G2 Black Payment Voucher": "G2 FZ Payment Voucher",
}

DEFAULT_PRINT_FORMATS: dict[str, str] = {
	"Purchase Order": "G2 Purchase Order",
	"Sales Invoice": "G2 Sales Invoice",
	"Quotation": "G2 Quotation",
	"Sales Order": "G2 Sales Order",
	"Delivery Note": "G2 Delivery Note",
	"Purchase Invoice": "G2 Purchase Invoice",
	"Purchase Receipt": "G2 Purchase Receipt",
	"Payment Entry": "G2 Payment Voucher",
	"Payment Voucher": "G2 Payment Voucher Bulk",
	"Expense Entry": "G2 Expense Entry",
	"Payment Request": "G2 Payment Request",
	"Proforma Invoice": "G2 Proforma Invoice",
	"Quote": "G2 Quote",
	"Consolidated Proforma Invoice": "G2 Consolidated Proforma Invoice",
	"Journal Entry": "G2 Journal Entry",
	"Salary Slip": "G2 Pay Slip",
}

# Report print uses frappe.client.get_value("Print Format", …) which needs Read.
# Desk User only has Select; grant Read/Print to roles that run financial reports.
PRINT_FORMAT_ROLE_PERMS: tuple[dict, ...] = (
	{
		"role": "Accounts Manager",
		"perms": {"select": 1, "read": 1, "print": 1, "export": 1},
	},
)


def after_install():
	import frappe

	sync_print_formats()
	set_default_print_formats()
	sync_print_format_permissions()


def after_migrate():
	import frappe

	sync_print_formats()
	set_default_print_formats()
	sync_print_format_permissions()


def before_uninstall():
	import frappe

	remove_default_print_formats()
	remove_print_format_permissions()
	names_to_remove = (
		{fmt["name"] for fmt in PRINT_FORMATS}
		| {fmt["name"] for fmt in REPORT_PRINT_FORMATS}
		| set(LEGACY_PRINT_FORMAT_RENAMES)
	)
	for name in names_to_remove:
		if frappe.db.exists("Print Format", name):
			frappe.delete_doc("Print Format", name, force=True, ignore_permissions=True)


def sync_print_format_permissions():
	"""Grant Print Format Read so Accounts Manager can load report print HTML."""
	import frappe
	from frappe.permissions import add_permission, update_permission_property

	doctype = "Print Format"
	for entry in PRINT_FORMAT_ROLE_PERMS:
		role = entry["role"]
		if not frappe.db.exists("Role", role):
			continue

		exists = frappe.db.exists(
			"Custom DocPerm",
			{"parent": doctype, "role": role, "permlevel": 0, "if_owner": 0},
		)
		if not exists:
			add_permission(doctype, role, 0, ptype="read")

		for ptype, value in entry["perms"].items():
			update_permission_property(doctype, role, 0, ptype, value, validate=False)

	frappe.clear_cache(doctype=doctype)


def remove_print_format_permissions():
	"""Remove only Custom DocPerm rows this app added for Print Format."""
	import frappe

	for entry in PRINT_FORMAT_ROLE_PERMS:
		name = frappe.db.get_value(
			"Custom DocPerm",
			{"parent": "Print Format", "role": entry["role"], "permlevel": 0, "if_owner": 0},
		)
		if name:
			frappe.delete_doc("Custom DocPerm", name, force=True, ignore_permissions=True)


def _doctype_exists(doctype: str) -> bool:
	import frappe

	return bool(doctype and frappe.db.exists("DocType", doctype))


def _drop_print_formats_for_missing_doctypes():
	"""Remove G2 print formats whose target DocType is not installed (e.g. Quote)."""
	import frappe

	for fmt in PRINT_FORMATS:
		if _doctype_exists(fmt["doc_type"]):
			continue
		if frappe.db.exists("Print Format", fmt["name"]):
			frappe.delete_doc("Print Format", fmt["name"], force=True, ignore_permissions=True)

	for doctype, print_format in DEFAULT_PRINT_FORMATS.items():
		if _doctype_exists(doctype):
			continue
		setter = frappe.db.get_value(
			"Property Setter",
			{
				"doc_type": doctype,
				"property": "default_print_format",
				"value": print_format,
			},
			"name",
		)
		if setter:
			frappe.delete_doc("Property Setter", setter, force=True, ignore_permissions=True)


def _rename_legacy_print_formats():
	"""Rename legacy G2 Black print formats to G2 FZ."""
	import frappe

	for old_name, new_name in LEGACY_PRINT_FORMAT_RENAMES.items():
		if not frappe.db.exists("Print Format", old_name):
			continue
		if frappe.db.exists("Print Format", new_name):
			frappe.delete_doc("Print Format", old_name, force=True, ignore_permissions=True)
		else:
			frappe.rename_doc("Print Format", old_name, new_name, force=True, show_alert=False)


def sync_print_formats():
	"""Create or update G2 custom print formats from template files."""
	import frappe

	previous_in_migrate = getattr(frappe.flags, "in_migrate", False)
	frappe.flags.in_migrate = True
	try:
		_sync_print_formats()
	finally:
		frappe.flags.in_migrate = previous_in_migrate


def _sync_print_formats():
	"""Internal sync implementation; requires in_migrate for standard formats."""
	import frappe

	_rename_legacy_print_formats()
	_drop_print_formats_for_missing_doctypes()
	for fmt in PRINT_FORMATS:
		if not _doctype_exists(fmt["doc_type"]):
			continue

		html = _read_compiled_template(fmt["html_file"])
		if not html:
			continue

		css = _read_template(fmt.get("css_file") or "g2_styles.css")

		if frappe.db.exists("Print Format", fmt["name"]):
			doc = frappe.get_doc("Print Format", fmt["name"])
		else:
			doc = frappe.new_doc("Print Format")
			doc.name = fmt["name"]

		doc.update(
			{
				"doc_type": fmt["doc_type"],
				"module": MODULE,
				"standard": "Yes",
				"custom_format": 1,
				"disabled": 0,
				"print_format_type": "Jinja",
				"print_format_for": "DocType",
				"print_format_builder": 0,
				"raw_printing": 0,
				"font_size": 11,
				"margin_top": 10.0,
				"margin_bottom": 10.0,
				"margin_left": 10.0,
				"margin_right": 10.0,
				"html": html,
				"css": css,
			}
		)
		doc.save(ignore_permissions=True)
		if fmt.get("finance_book") and doc.meta.has_field("finance_book"):
			doc.db_set("finance_book", fmt["finance_book"], update_modified=False)

	_sync_report_print_formats()

	frappe.clear_cache()
	normalize_git_json_files()


def _sync_report_print_formats():
	"""Create or update G2 report print formats (Query Report JS templates)."""
	import frappe

	for fmt in REPORT_PRINT_FORMATS:
		html = _read_compiled_template(fmt["html_file"])
		if not html:
			continue

		if frappe.db.exists("Print Format", fmt["name"]):
			doc = frappe.get_doc("Print Format", fmt["name"])
		else:
			doc = frappe.new_doc("Print Format")
			doc.name = fmt["name"]

		# Report formats: before_save forces custom_format=1 and standard=No
		doc.update(
			{
				"doc_type": "",
				"report": fmt["report"],
				"module": MODULE,
				"standard": "No",
				"custom_format": 1,
				"disabled": 0,
				"print_format_type": "JS",
				"print_format_for": "Report",
				"print_format_builder": 0,
				"raw_printing": 0,
				"font_size": 8,
				"margin_top": 8.0,
				"margin_bottom": 8.0,
				"margin_left": 8.0,
				"margin_right": 8.0,
				"page_number": "Hide",
				"pdf_generator": "chrome",
				"html": html,
				"css": "",
			}
		)
		doc.save(ignore_permissions=True)


def export_print_format_fixtures():
	"""Export fixtures and normalize timestamps for stable git diffs."""
	import frappe
	from frappe.utils.fixtures import sync_fixtures

	sync_fixtures(app=APP_NAME)
	normalize_git_json_files()


def normalize_git_json_files(app_root: str | None = None) -> list[str]:
	"""Normalize creation/modified timestamps in exported JSON for stable git diffs."""
	if app_root is None:
		app_root = os.path.dirname(os.path.abspath(__file__))

	updated_files: list[str] = []
	json_paths = [
		os.path.join(app_root, "fixtures", "print_format.json"),
		os.path.join(app_root, "fixtures", "property_setter.json"),
		os.path.join(app_root, "fixtures", "custom_docperm.json"),
	]

	print_format_root = os.path.join(app_root, "g2_print_formats", "print_format")
	if os.path.isdir(print_format_root):
		for folder in os.listdir(print_format_root):
			json_path = os.path.join(print_format_root, folder, f"{folder}.json")
			if os.path.isfile(json_path):
				json_paths.append(json_path)

	for path in json_paths:
		if _normalize_json_file(path):
			updated_files.append(path)

	return updated_files


def _normalize_json_file(path: str) -> bool:
	if not os.path.isfile(path):
		return False

	with open(path, encoding="utf-8") as handle:
		data = json.load(handle)

	changed = _normalize_json_timestamps(data)
	if not changed:
		return False

	with open(path, "w", encoding="utf-8") as handle:
		json.dump(data, handle, indent=1, ensure_ascii=False)
		handle.write("\n")

	return True


def _normalize_json_timestamps(data) -> bool:
	if isinstance(data, list):
		changed = False
		for item in data:
			if _normalize_json_timestamps(item):
				changed = True
		return changed
	if isinstance(data, dict):
		changed = False
		for field in GIT_TIMESTAMP_FIELDS:
			if field in data and data[field] != STABLE_GIT_TIMESTAMP:
				data[field] = STABLE_GIT_TIMESTAMP
				changed = True
		for value in data.values():
			if isinstance(value, (dict, list)) and _normalize_json_timestamps(value):
				changed = True
		return changed
	return False


def set_default_print_formats():
	"""Set G2 print formats as the default for supported doctypes."""
	import frappe

	for doctype, print_format in DEFAULT_PRINT_FORMATS.items():
		if not _doctype_exists(doctype):
			continue
		if not frappe.db.exists("Print Format", print_format):
			continue

		frappe.make_property_setter(
			{
				"doctype": doctype,
				"doctype_or_field": "DocType",
				"property": "default_print_format",
				"value": print_format,
				"property_type": "Data",
			},
			validate_fields_for_doctype=False,
		)

	frappe.clear_cache()


def remove_default_print_formats():
	import frappe

	for doctype, print_format in DEFAULT_PRINT_FORMATS.items():
		property_setter = frappe.db.get_value(
			"Property Setter",
			{
				"doc_type": doctype,
				"property": "default_print_format",
				"value": print_format,
			},
			"name",
		)
		if property_setter:
			frappe.delete_doc("Property Setter", property_setter, force=True, ignore_permissions=True)

	frappe.clear_cache()


def _read_compiled_template(filename: str) -> str:
	"""Read a print template and inline shared partials for reliable PDF rendering."""
	content = _read_template(filename)
	for partial in TEMPLATE_PARTIALS:
		partial_content = _read_template(partial)
		if partial_content:
			content = content.replace(
				f'{{% include "templates/print_formats/{partial}" %}}',
				partial_content,
			)
	return content


def _read_template(filename: str) -> str:
	import frappe

	path = os.path.join(frappe.get_app_path(APP_NAME), TEMPLATE_DIR, filename)
	if not os.path.exists(path):
		frappe.log_error(f"G2 print template missing: {path}", "G2 Print Formats")
		return ""
	with open(path, encoding="utf-8") as handle:
		return handle.read()


if __name__ == "__main__":
	updated = normalize_git_json_files()
	if updated:
		print(f"Normalized timestamps in {len(updated)} file(s).")
	else:
		print("No timestamp changes needed.")
