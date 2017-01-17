---
Description: PROPERTYKEYs and GUIDs in Windows Portable Devices
MS-HAID: 'wpddk.propertykeys\_and\_guids\_in\_windows\_portable\_devices'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: PROPERTYKEYs and GUIDs in Windows Portable Devices
---

# PROPERTYKEYs and GUIDs in Windows Portable Devices


A property or command is identified by a **PROPERTYKEY** structure. A **PROPERTYKEY** structure is made up of two parts: a GUID (the *fmtid* member) and a DWORD (the *pid* member). The GUID part is used to indicate the category the property or command belongs to (that is, related properties belong to the same category and related commands belong to the same category; therefore they will have the same *fmtid*). The DWORD part indicates the property or command ID, and is used to distinguish the individual properties or commands within a property or command category (that is, the *pid* values for properties or commands in the same category will be different).

The reference section of this document describes all the PROPERTYKEY values defined by WPD. These values correspond to commands, properties, and resources. If you create a custom PROPERTYKEY value, you should define a new GUID category; do not reuse the WPD GUID values or you risk conflicting with existing and future WPD-specified PROPERTYKEYs.

## <span id="related_topics"></span>Related topics


[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff597845)

[**Requirements for Objects**](requirements-for-objects.md)

[**Object Format GUIDs**](https://msdn.microsoft.com/library/windows/hardware/ff597651)

[**Requirements for Resources**](https://msdn.microsoft.com/library/windows/hardware/ff597663)

[**Commands**](https://msdn.microsoft.com/library/windows/hardware/ff597554)

[**Properties and Attributes**](https://msdn.microsoft.com/library/windows/hardware/ff597900)

[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20PROPERTYKEYs%20and%20GUIDs%20in%20Windows%20Portable%20Devices%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




