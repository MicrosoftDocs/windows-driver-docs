---
title: PnPUtil Return Values
description: PnPUtil Return Values
ms.date: 12/28/2023
---

# PnPUtil Return Values

This page lists some of the values that the PnPUtil tool returns.  For info on other possible values, see [Error Codes](/windows/win32/debug/system-error-codes).

* `ERROR_SUCCESS` (0): The requested operation completed successfully.
* `ERROR_NO_MORE_ITEMS` (259): No devices match the supplied driver or the target device is already using a better or newer driver than the driver specified for installation. 
* `ERROR_SUCCESS_REBOOT_REQUIRED` (3010): The requested operation completed successfully and a system reboot is required.  For example, if the  `/install /add-driver` options were specified, one or more devices were successfully installed and a system reboot is required to finalize installation.
* `ERROR_SUCCESS_REBOOT_INITIATED` (1641): The operation was successful and a system reboot is underway because the `/reboot` option was specified.

While you can still use PnPUtil to bulk install drivers, to get actionable return values we recommend specifying `/install /add-driver` with one INF at a time.

Here are some additional troubleshooting best practices:

* If the `/add-driver` and `/delete-driver` options were specified, check `%windir%\inf\setupapi.dev.log` for more information.

* If the `/enable-device` and `/disable-device` options were specified, set the SetupAPI log verbosity to full (`0x2000ffff`) and re-attempt the operation.  If it fails again, check `%windir%\inf\setupapi.app.log` for more information. For info on verbosity levels, see [Setting SetupAPI Logging Levels](../install/setting-setupapi-logging-levels.md).

## See also

[PnPUtil](pnputil.md)

[PnPUtil Command Syntax](pnputil-command-syntax.md)