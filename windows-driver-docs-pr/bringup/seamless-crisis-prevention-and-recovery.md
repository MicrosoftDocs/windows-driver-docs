---
title: Seamless crisis prevention and recovery
description: If a firmware update fails, the results can be devastating.
ms.assetid: F002100E-2505-4CCB-B048-27D9CA1C8F3E
ms.date: 08/06/2018
ms.localizationpriority: medium
---

# Seamless crisis prevention and recovery


If a firmware update fails, the results can be devastating. At best, the update fails, but the system is resilient and recovers without the end-user becoming aware. At worst, it is possible for a failed firmware update to result in a completely unusable system, requiring the end-user to return their system to the retailer or manufacturer for repair. The latter case is what we call a *crisis*.

A crisis can result from a failed firmware update, or due to firmware that is incompatible with Windows or other aspects of the system. This section discusses features designed to prevent and recover from crises that resulting from failed firmware updates. Our expectation is that firmware update test coverage by the firmware author will prevent the majority of crises resulting from incompatible firmware.

In order to provide a great experience for end-users, the following crisis prevention and recovery requirements must be met for the firmware driver package update mechanism. These requirements do not preclude additional crisis prevention or recovery solutions.

## Pre-installation criteria


When the system firmware is performing the actual update there are a series of pre-installation checks that must be performed. System firmware must perform this check to ensure there is enough power to complete the update. It is also recommended that the checks be made for each of the updates before the update is applied if there are multiple firmware updates. The list of items to check and validate are provided below. All of the checks must be performed where applicable. There is no specific order to the execution of the tests.

<table>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<thead>
<tr class="header">
<th>Check type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Power</td>
<td><ul>
<li>System must have at least 25% battery charge.</li>
<li>Tethered power (power via USB cable and/or AC power) is not required.</li>
</ul>
<div class="alert">
<strong>Note</strong>  In a test/laboratory environment it is acceptable to have no battery present yet still allow firmware updates as long as tethered power is provided. However a differentiation must be made between a dead/not charging battery and no battery present.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td>Security</td>
<td><ul>
<li>Validate update capsule payload is properly signed.</li>
<li>Validate that any PE-based EFI files in the payload are properly signed with a proper EFI cert.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Integrity</td>
<td><p>Perform an integrity check on the firmware update payload.</p></td>
</tr>
<tr class="even">
<td>Version</td>
<td><p>Verify that the firmware being applied does not downgrade the current, installed firmware beyond the LowestSupportedFirmwareVersion value.</p></td>
</tr>
<tr class="odd">
<td>Storage</td>
<td><p>The following checks are performed as appropriate, depending upon the system’s hardware</p>
<ul>
<li>There is sufficient room for backups of the current firmware which will be replaced</li>
<li>There is sufficient room in the device to accommodate the new firmware</li>
</ul></td>
</tr>
</tbody>
</table>

 

Any failure must result in an appropriate Last Attempt Status error code. For more information, see the Last Attempt Status error code information in [ESRT table definition](esrt-table-definition.md) and [Firmware update status](firmware-update-status.md).

If multiple updates are being applied and some pass the pre-installation checks and others do not, platform firmware can proceed with updating the firmware for the resources that passed the pre-installation checks. However, any resource that failed the pre-installation check must not be updated.

## Post-installation criteria

After firmware (device or system) has been installed it must be checked to validate that the new updated firmware image is what was intended. This is to minimize any risks of any corruption introduced during the actual updating process (for example sticky bits in flash ROM, noise on a bus during the updating and so on).

The updating process must validate that the updated firmware passes integrity checks. If it fails then it must recover by rolling back to the last known good version of the firmware.

Any failure must result in an appropriate Last Attempt Status error code. For more information, see the Last Attempt Status error code information in [ESRT table definition](esrt-table-definition.md) and [Firmware update status](firmware-update-status.md).

## Recovering from install and boot failures

In order to prevent a system from reaching a non-bootable state, the firmware update mechanism must meet the following requirements in cases where firmware updates fail to install, or in cases where the system fails to boot successfully.

> [!NOTE]
> In the following sections, the term "committed" is used to describe firmware. Once firmware has been "committed", the firmware is treated as fully installed, and will not be automatically rolled back by the firmware due to boot failure, etc. "Uncommitted" firmware describes partially updated firmware and can potentially be rolled back to a previous version in cases where the firmware update cannot be completed or a failure is detected by the updating firmware (for example, invalid CRC check in the update). Whether firmware is committed is something that the firmware should track internally, and is not captured as part of the ESRT.

### Firmware update unsuccessful

If an individual system or device firmware cannot be installed, or has been installed incorrectly (e.g. due to some kind of corruption, or a power loss while installing the update), the update may be retried up to a total of three (3) attempts, including the first attempt. If additional retry attempts will be performed by the firmware, the system must not boot into Windows between any of the attempts. If all attempts fail, the updating firmware must discard the update. If the update was partially applied, the firmware must roll back to the previous version. The firmware must roll back to the previous version without any user interaction. The update failure does not affect other pending updates; pending firmware updates should be attempted.

After all of the updates have been processed, UEFI will resume booting Windows. The UEFI firmware must verify that any non-committed firmware updates were successfully installed in order to mitigate problems due to power loss (UEFI should never attempt to boot Windows with partially written firmware).

Possible causes for install failure include, but are not limited to:

-   Insufficient resources
-   Power loss
-   Hardware failure

### Firmware update succeeds but Windows fails to boot

The UEFI firmware is not responsible for rolling back updated firmware once it has been committed. Existing failover logic in Windows will divert the end-user to the Windows Recovery Environment (WinRE) after two unsuccessful boot attempts. WinRE may or may not boot successfully. The end-user will have to take a manual recovery step to recover their system, or will have to return their device to the retailer/manufacturer.

Possible causes for this class of failure include, but are not limited to:

-   Firmware incompatible with OS drivers.
-   Firmware incompatible with OS components.

If a hardware vendor decides to implement additional logic to determine whether Windows has successfully booted, that is acceptable. As mentioned previously, the expectation is that firmware update test coverage by the firmware author will prevent the majority of crises resulting from incompatible firmware.

## Related topics
[ESRT table definition](esrt-table-definition.md)  
[Plug and play device](plug-and-play-device.md)  
[Authoring an update driver package](authoring-an-update-driver-package.md)  
[Processing updates](processing-updates.md)  
[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  
[Firmware update status](firmware-update-status.md)  
