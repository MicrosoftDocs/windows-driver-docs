---
title: Configuring Windows to Rank Driver Signatures Equally
description: Configuring Windows to Rank Driver Signatures Equally
ms.assetid: 727ad66d-b8f3-4e22-b51f-af9571ae0ec8
---

# Configuring Windows to Rank Driver Signatures Equally


The [AllSignersEqual Group Policy](allsignersequal-group-policy--windows-vista-and-later-.md) controls [how Windows ranks drivers](how-setup-ranks-drivers.md) that are signed by Microsoft versus drivers that are signed by third-party vendors. When the AllSignersEqual Group Policy is enabled, Windows views all Microsoft signature types and third-party signatures as equal in rank when it selects the driver that is the best match for a device.

**Note**  In Windows Vista and Windows Server 2008, the **AllSignersEqual** Group Policy is disabled by default. Starting with Windows 7, this Group Policy is enabled by default.

 

After you enable the AllSignersEqual Group Policy, this configuration change applies to all subsequent driver installations on the target system until you disable the AllSignersEqual Group Policy.

For more information about how to configure the **AllSignersEqual** Group Policy to rank driver signatures equally, see [AllSignersEqual Group Policy (Windows Vista and Later)](allsignersequal-group-policy--windows-vista-and-later-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Configuring%20Windows%20to%20Rank%20Driver%20Signatures%20Equally%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




