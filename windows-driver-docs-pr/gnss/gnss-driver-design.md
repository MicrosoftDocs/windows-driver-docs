---
title: GNSS driver design
author: windows-driver-content
description: Discusses design principles to consider when developing a GNSS driver for Windows 10 including data structures, error reporting, and driver versioning.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: E10B1149-CC8B-438D-B537-258F7FCFA0E7
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20GNSS%20driver%20design%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


