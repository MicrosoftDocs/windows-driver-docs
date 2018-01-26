---
title: MSFC\_DH\_Chap\_Parameters WMI Class
description: MSFC\_DH\_Chap\_Parameters WMI Class
ms.assetid: 259E3935-0F37-4DBE-BED3-C55A6715A810
---

# MSFC\_DH\_Chap\_Parameters WMI Class


A WMI client uses the **MSFC\_DH\_Chap\_Parameters** class to set the response parameters for a CHAP challenge on a virtual port.

The **MSFC\_DH\_Chap\_Parameters** class is defined as follows in *Npivwmi.mof*:

```mof
class MSFC_DH_Chap_Parameters
{    
    [WmiDataId(1),
     Description("Length in bytes of the shared secret."):Amended]
    uint32 SharedSecretLength;
   
    [WmiDataId(2),
    Description("Shared Secret Encoding"):Amended,
     ValueMap {"1", "2"},
     Values {"Printable ASCII", "Binary"}]
    uint8 SecretEncoding;

    [WmiDataId(3),
     WmiSizeIs("SharedSecretLength"),
     Description("Shared secret to be used at the basis of a DH-CHAP challenge."):Amended]
    uint8 SharedSecret[];
};
```

When compiled by the WMI tool suite, this class definition produces the following data structure:

**MSFC\_DH\_Chap\_Parameters**

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_DH_Chap_Parameters%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




