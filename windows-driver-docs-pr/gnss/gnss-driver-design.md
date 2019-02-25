---
title: GNSS driver design
description: Discusses design principles to consider when developing a GNSS driver for Windows 10 including data structures, error reporting, and driver versioning.
ms.assetid: E10B1149-CC8B-438D-B537-258F7FCFA0E7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GNSS driver design


Discusses design principles to consider when developing a GNSS driver for Windows 10 including data structures, error reporting, and driver versioning.

## Data structures


For backward compatibility and future extensibility, all data structures begin with a version number and size to accommodate future extensions and backward compatibility issues. As an additional safeguard, each structure also has a padding buffer to keep the static structure size the same even when new fields are added. This is to protect against any older GNSS drivers mistakenly using the static compile-time size of the structure (using **sizeof**) instead of the dynamic size of the structure.

Unless otherwise specified, all parameters will follow the International System of Units (SI):

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameters</th>
<th>Units</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Distance, threshold, or level</p></td>
<td><p><strong>meter</strong></p></td>
</tr>
<tr class="even">
<td><p>Timeout or interval</p></td>
<td><p><strong>second</strong></p></td>
</tr>
<tr class="odd">
<td><p>Speed</p></td>
<td><p><strong>meter/second</strong></p></td>
</tr>
</tbody>
</table>

 

## Error reporting


The GNSS DDI expects an **NTSTATUS** as a return value from the driver. The high level operating system (HLOS) acts on only success and failure cases based on these error messages and does not look at a specific error message. Still it is preferred that the driver returns errors closely mapped to the corresponding **NTSTATUS** error message. The GNSS driver can send its own custom **NTSTATUS** error messages which could be helpful for diagnostic purposes.

## Driver versioning


Every structure specified for the GNSS DDI contains a driver version field, and many structures contain a padding field. Both of these components are used to mitigate new versions of the GNSS DDI, using the following policies:

-   The framework and the driver communicate their respective versions using the capability exchange process. These IOCTLs are considered special in that they communicate their versions using the version field. Therefore, implementations surrounding device and platform capability checking should explicitly check the versions returned first, and store it for usage later. The version member of the [**GNSS\_DEVICE\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/dn925104) structure communicates the version number of the driver. The version member of the [**GNSS\_PLATFORM\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/dn925205) structure communicates the version number of the GNSS adapter.

-   Whenever a new field is added, if the structure has a padding field, space shall be taken out of padding instead of adding to the structure, which will maintain binary compatibility

-   Whenever a new field is added, the version of the GNSS DDI is considered incremented. This will be reflected in a comment in the GNSS DDI header itself, but NOT exposed as a constant. Both the GNSS adapter and the GNSS driver will use private constant values to indicate its current version. This allows both the GNSS adapter and the driver to be coded against a specific version.

-   The GNSS adapter must be backward compatible with older versions of the GNSS driver. If a protocol change is introduced in a new version of the DDI, a GNSS adapter compliant with the new GNSS DDI must implement the new protocol only for the new version of the driver, and use the old protocol for older version of the driver.

-   The GNSS driver must be forward compatible with newer versions of the GNSS adapter and should treat newer versions of the GNSS adapter in the same manner as current version that it is coded against.

-   An older version of the GNSS adapter is not expected to function correctly with a newer version of the GNSS driver. To facilitate co-development of the GNSS adapter and the GNSS driver against a new version of the DDI, no strict version check will exist in the GNSS adapter to block newer GNSS drivers. However, a GNSS driver implemented against a newer version of the DDI will not be shipped to retail devices that contain a GNSS adapter implemented against an older version of the GNSS DDI.

-   Any Windows 8.1 or older GNSS sensor drivers will not be supported by the GNSS adapter. These drivers would continue to function in Windows 10 through the legacy stack. In presence of another Windows 10 GNSS driver the usage of the legacy GNSS sensor driver is undefined.

 

 




