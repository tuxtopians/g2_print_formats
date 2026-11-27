def g2_print_doc_number(name, doc=None):
	"""Return document number without Frappe amendment revision suffix."""
	if not name:
		return name or ""

	if doc and doc.get("amended_from"):
		base, suffix = name.rsplit("-", 1)
		if suffix.isdigit():
			return base

	return name
