---
title: MSFC\_DH\_Chap\_Parameters WMI Class
description: MSFC\_DH\_Chap\_Parameters WMI Class
ms.assetid: 259E3935-0F37-4DBE-BED3-C55A6715A810
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 





