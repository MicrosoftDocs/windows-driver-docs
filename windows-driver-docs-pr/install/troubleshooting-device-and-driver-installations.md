---
title: Troubleshooting Device and Driver Installations
description: Use these guidelines to verify that your device is installed correctly or diagnose problems with your device installation.
keywords:
- Device setup WDK device installations , troubleshooting
- device installations WDK, troubleshooting
- installing devices WDK, troubleshooting
- troubleshooting device installations WDK
- Device setup WDK device installations, SetupAPI
- installing devices WDK, SetupAPI
ms.date: 12/05/2022
---

# Troubleshooting Device and Driver Installations

You can use the following guidelines to either verify that your device is installed correctly or diagnose problems with your device installation.

## Check if the device is marked with a problem

If the device has a [problem code](devpkey-device-problemcode.md) set, then something may have gone wrong during device installation or with the settings/configuration of the device. To check if the device has a problem code set, you can [use Device Manager](using-device-manager.md) to check if the device's icon has an overlay of a yellow triangle with an exclamation mark.  Launching the Properties dialog for the device will provide what the problem code value is, along with an error message.

You can also check if the device has a problem code set via the command line with [PnPUtil](../devtest/pnputil.md).  If you know the [device instance path](device-instance-ids.md) of your device, you can use PnPUtil to check its status:

```console
pnputil /enum-devices /instanceid <device instance path>
```

If you don't know the device instance path of your device, you can use PnPUtil to check if any devices have a problem code set and you can see if any of those look like your device:

```console
pnputil /enum-devices /problem
```

If you identify that the device has a problem code set, see [Device Manager Error Message](device-manager-error-messages.md) for more information on the problem code.

## Look at device installation logs

You can follow the steps that are described in [SetupAPI Logging (Windows Vista and Later)](setupapi-logging--windows-vista-and-later-.md) or [SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)](setupapi-logging--windows-server-2003--windows-xp--and-windows-2000-.md) to identify device installation errors. See below for a list of common installation errors:

| Error code | Description |
|---|---|
| 0x000005B4 (ERROR_TIMEOUT) | The device installation took too long and was stopped.  See [SetupApi logs](setupapi-text-logs.md) for more information about the device installation and where the time was spent.<br><br>Some common causes of timeouts are:<br><br>A co-installer executing for too long.  This could be because the co-installer is performing some unsupported operation that has hung or is too long running.  For example, a co-installer is executed in a non-interactive session, so it can't do something that needs to wait on user input.  Co-installers are deprecated and should be avoided. For more information, see [universal INFs](using-a-universal-inf-file.md).<br><br>Starting or restarting a device at the end of device installation has hung. |
| 0xe0000219 (ERROR_NO_ASSOCIATED_SERVICE) | The driver package being installed on the device didn't specify an associated service for the device.  For more information, see the SPSVCINST_ASSOCSERVICE flag in the [INF AddService Directive](inf-addservice-directive.md) documentation. |
| 0xe0000248 (ERROR_DEVICE_INSTALL_BLOCKED) | The installation of the device was blocked due to group policy settings.  For more information, see [controlling device installation using Group Policy](/previous-versions/dotnet/articles/bb530324(v=msdn.10)) and [Mobile Device Management policies for device installation](/windows/client-management/mdm/policy-csp-deviceinstallation). |
| 0x000001e0 (ERROR_PNP_QUERY_REMOVE_DEVICE_TIMEOUT) | At the end of device installation, one or more devices will be restarted to pick up new files or settings changed during the device installation.  As part of this restart operation, a query remove operation is performed on the device or devices being restarted. This error indicates that something hung or took too long during the query remove operation for the device being installed. For more information, see [SetupApi logs](setupapi-text-logs.md). |
| 0x000001e1 (ERROR_PNP_QUERY_REMOVE_RELATED_DEVICE_TIMEOUT) | At the end of device installation, one or more devices will be restarted to pick up new files or settings changed during the device installation.  As part of this restart operation, a query remove operation is performed on the device or devices being restarted. This error indicates that something hung or took too long during the query remove operation for one of the device or devices being restarted. For more information, see [SetupApi logs](setupapi-text-logs.md). |
| 0x000001e2 (ERROR_PNP_QUERY_REMOVE_UNRELATED_DEVICE_TIMEOUT) | At the end of device installation, one or more devices will be restarted to pick up new files or settings changed during the device installation.  As part of this restart operation, a query remove operation is performed on the device or devices being restarted. This error indicates that that query remove operation wasn't able to be performed in a timely manner due to a query remove operation being performed on another device on the system. For more information, see [SetupApi logs](setupapi-text-logs.md). |

## Debug a class installer or co-installer during installation

> [!NOTE]
> Class installers and co-installers are deprecated.  For more information, see [Universal INFs](using-a-universal-inf-file.md).

On Windows Vista and later versions of Windows, follow the steps that are described in [Debugging Device Installations (Windows Vista and Later)](debugging-device-installations--windows-vista-and-later-.md) to debug class installers or [co-installers](writing-a-co-installer.md) during the core stages of device installation.
