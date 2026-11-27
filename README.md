# G2 Print Formats

Shared G2 / G2 FZ Jinja print formats and report print templates synced on migrate.

## Overview

| | |
|---|---|
| **App name** | `g2_print_formats` |
| **Module(s)** | `G2 Print Formats` |
| **Publisher** | Savad Ibrahim |
| **Required apps** | `erpnext` |
| **Installed on (this bench)** | g2technology, site1.local |
| **License** | mit |

## Install / Setup

```bash
cd /home/frappe/frappe-bench
# If not already on the bench:
# bench get-app <repo-url> --branch <current-branch>
bench --site <site> install-app g2_print_formats
bench --site <site> migrate
```

Export fixtures after changing Custom Fields / Property Setters (when the app uses fixtures):

```bash
bench --site <site> export-fixtures --app g2_print_formats
```

## Features

- Partials under templates/print_formats/; install.sync_print_formats inlines into Print Format HTML
- Skips formats whose DocType is not installed; legacy G2 Black → G2 FZ rename on sync
- Report prints: G2 Monthly Profit and Loss, G2 Balance Sheet, G2 Party Ledger (General Ledger default), G2 Customer Outstanding (Accounts Receivable default), G2 Outstanding Invoices (Accounts Receivable Report default), G2 Outstanding Payables (Accounts Payable Report default); Accounts Manager Print Format perms
- Re-sync: bench --site <site> execute g2_print_formats.install.sync_print_formats

## DocTypes

_None (customizations / fixtures / UI only)._

## Desk Pages

_None._

## Reports

_None._

## APIs (`@frappe.whitelist`)

_No `@frappe.whitelist` methods found (or none exported)._ 

## Hooks / Fixtures

- `after_install` → `g2_print_formats.install.after_install`
- `after_migrate` → `g2_print_formats.install.after_migrate`
- `before_uninstall` → `g2_print_formats.install.before_uninstall`
- Fixture files: `custom_docperm.json`, `print_format.json`, `property_setter.json`

## Configuration

- Prefer site **g2technology** (default site) or **site1.local** when testing Biztek/G2 customizations.
- Base behavior on `hooks.py`, DocType JSON, and fixtures under the app package — do not assume undocumented side effects.

## Uninstall / Cleanup

This app defines uninstall hooks — prefer `bench --site <site> uninstall-app g2_print_formats` so custom fields, nav, and fixtures are cleaned.

## Documentation source

Generated/updated from package inventory on 2026-09-08 (hooks, DocTypes, pages, reports, whitelisted methods). Cross-checked against bench OpenMemory guide where available.
