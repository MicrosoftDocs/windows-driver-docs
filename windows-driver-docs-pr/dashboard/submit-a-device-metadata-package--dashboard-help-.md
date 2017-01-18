---
title: Submit a Device Metadata Package (Dashboard help)
description: Submit a Device Metadata Package (Dashboard help)
MS-HAID:
- 'p\_dashboard.submit\_a\_device\_metadata\_package\_\_dashboard\_help\_'
- 'hw\_dashboard.submit\_a\_device\_metadata\_package\_\_dashboard\_help\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dcd35784-51c3-410a-8704-94f07fa8959a
---

# Submit a Device Metadata Package (Dashboard help)


After you have created a new device metadata package or replaced an existing package, you can submit the package for validation and subsequent publication.

## <span id="Submitting_a_device_metadata_package"></span><span id="submitting_a_device_metadata_package"></span><span id="SUBMITTING_A_DEVICE_METADATA_PACKAGE"></span>Submitting a device metadata package


You can use the same method to submit packages for preview or release.

**To submit a device metadata package**

1.  Sign the metadata package with the [SignTool tool](http://go.microsoft.com/fwlink/p/?LinkId=238330).

2.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

3.  Under **Device metadata**, click either **Create experience** (if you want to submit a new experience), or **Manage experience** (if you want to modify an existing experience).

4.  Browse for and select your new experience, and then click **Submit**.

For more information, see [Create a Device Metadata Experience](https://msdn.microsoft.com/library/windows/hardware/br230794.aspx) or [Manage Device Metadata Experiences](https://msdn.microsoft.com/library/windows/hardware/br230797.aspx).

During the submission process, the dashboard validates the packages in your experience.

### <span id="Package_validation"></span><span id="package_validation"></span><span id="PACKAGE_VALIDATION"></span>Package validation

During validation, the dashboard performs the following actions for each package:

-   Confirms the file is code-signed.

-   Scans for viruses.

-   Checks the package structure.

-   Validates all .xml files against the appropriate schema.

-   Verifies that all icons are in compliance with the designated Windows operating system.

-   Verifies that all relational fields in the .xml files point to existing resources.

-   Verifies that all required tasks and status elements are included in the DeviceStage packages.

-   Verifies that hardware certification submissions that are bound to a device experience are for the correct device.

-   Writes the date value into the package, and confirms the device experience.

-   Creates and signs .cat files in each directory to indicate validation.

-   Reconstructs the package and renames it as a GUID.

-   Signs the device metadata package.

### <span id="Submitting_a_service_metadata_package"></span><span id="submitting_a_service_metadata_package"></span><span id="SUBMITTING_A_SERVICE_METADATA_PACKAGE"></span>Submitting a service metadata package

For info about submitting service metadata for a mobile broadband app, see [Service metadata package submission](https://msdn.microsoft.com/library/windows/hardware/dn247118.aspx).

## <span id="related_topics"></span>Related topics


[Create a Device Metadata Experience](https://msdn.microsoft.com/library/windows/hardware/br230794.aspx)

[Manage Device Metadata Experiences](https://msdn.microsoft.com/library/windows/hardware/br230797.aspx)

[Submit a Bulk Metadata Package](https://msdn.microsoft.com/library/windows/hardware/hh801895.aspx)

[Errors and Solutions When Submitting Device Metadata Experiences](https://msdn.microsoft.com/library/windows/hardware/br230786.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Submit%20a%20Device%20Metadata%20Package%20%28Dashboard%20help%29%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





