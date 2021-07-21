---
title: Troubleshooting Device and Driver Installations
description: Troubleshooting Device and Driver Installations
keywords:
- Device setup WDK device installations , troubleshooting
- device installations WDK , troubleshooting
- installing devices WDK , troubleshooting
- troubleshooting device installations WDK
- Device setup WDK device installations , SetupAPI
- installing devices WDK , SetupAPI
ms.date: 06/17/2021
ms.localizationpriority: medium
---

# Troubleshooting Device and Driver Installations





You can use the following guidelines to either verify that your device is installed correctly or diagnose problems with your device installation:

-   Follow the steps that are described in [Using Device Manager](using-device-manager.md) to view system information about the device.

-   Follow the steps that are described in [SetupAPI Logging (Windows Vista and Later)](setupapi-logging--windows-vista-and-later-.md) or [SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)](setupapi-logging--windows-server-2003--windows-xp--and-windows-2000-.md) to identify installation errors. See below for more information on common installation errors.

-   On Windows Vista and later versions of Windows, follow the steps that are described in [Debugging Device Installations (Windows Vista and Later)](debugging-device-installations--windows-vista-and-later-.md) to debug [co-installers](writing-a-co-installer.md) during the core stages of device installation.

-   On Windows Vista and later versions of Windows, follow the steps that are described in [Troubleshooting Install and Load Problems with Test-signed Drivers](./detecting-driver-load-errors.md) to diagnose problems related to the installation and loading of test-signed drivers.

-   Run test programs to exercise the device. This includes the testing and debugging tools that are supplied with the Windows Driver Kit (WDK).

Common device installation errors:

<table>
<colgroup>
<col width="40%" />
<col width="60%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x000005B4 (ERROR_TIMEOUT)</p></td>
<td align="left"><p>
The device installation took too long and was stopped.  See the <a href="setupapi-text-logs.md" data-raw-source="[SetupApi logs](setupapi-text-logs.md)">SetupApi logs</a> for more information about the device installation and where the time was spent. Some common causes of timeouts are:
<ul>
<li>A co-installer executing for too long.  This could be because the co-installer is performing some unsupported operation that has hung or is too long running.  For example, a co-installer is executed in a non-interactive session, so it cannot do something that needs to wait on user input.  Co-installers are deprecated and should be avoided.  See <a href="using-a-universal-inf-file.md" data-raw-source="[universal INFs](using-a-universal-inf-file.md)">universal INFs</a> for more information.</li>
<li>Starting a device at the end of device installation has hung.</li>
</ul>
</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xe0000219 (ERROR_NO_ASSOCIATED_SERVICE)</p></td>
<td align="left"><p>
The driver package being installed on the device did not specify an associated service for the device.  Please see the SPSVCINST_ASSOCSERVICE flag in the <a href="inf-addservice-directive.md" data-raw-source="[INF AddService Directive](inf-addservice-directive.md)">INF AddService Directive</a> documentation for more information.
</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xe0000248 (ERROR_DEVICE_INSTALL_BLOCKED)</p></td>
<td align="left"><p>
The installation of the device was blocked due to group policy settings.  For more information, see <a href="/previous-versions/dotnet/articles/bb530324(v=msdn.10)">controlling device installation using Group Policy</a> and <a href="/windows/client-management/mdm/policy-csp-deviceinstallation">Mobile Device Management policies for device installation</a>.
</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x000001e0 (ERROR_PNP_QUERY_REMOVE_DEVICE_TIMEOUT)</p></td>
<td align="left"><p>
At the end of device installation, one or more devices will be restarted to pick up new files or settings changed during the device installation.  As part of this restart operation, a query remove operation is performed on the device or devices being restarted. This error indicates that something hung or took too long during the query remove operation for the device being installed. See the <a href="setupapi-text-logs.md" data-raw-source="[SetupApi logs](setupapi-text-logs.md)">SetupApi logs</a> for more information.
</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x000001e1 (ERROR_PNP_QUERY_REMOVE_RELATED_DEVICE_TIMEOUT)</p></td>
<td align="left"><p>
At the end of device installation, one or more devices will be restarted to pick up new files or settings changed during the device installation.  As part of this restart operation, a query remove operation is performed on the device or devices being restarted. This error indicates that something hung or took too long during the query remove operation for one of the device or devices being restarted. See the <a href="setupapi-text-logs.md" data-raw-source="[SetupApi logs](setupapi-text-logs.md)">SetupApi logs</a> for more information.
</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x000001e2 (ERROR_PNP_QUERY_REMOVE_UNRELATED_DEVICE_TIMEOUT)</p></td>
<td align="left"><p>
At the end of device installation, one or more devices will be restarted to pick up new files or settings changed during the device installation.  As part of this restart operation, a query remove operation is performed on the device or devices being restarted. This error indicates that that query remove operation was not able to be performed in a timely manner due to a query remove operation being performed on another device on the system. See the <a href="setupapi-text-logs.md" data-raw-source="[SetupApi logs](setupapi-text-logs.md)">SetupApi logs</a> for more information.
</p></td>
</tr>
</tbody>
</table>


 

