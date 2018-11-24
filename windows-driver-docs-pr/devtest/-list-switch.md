---
title: /List Switch
description: The /List switch of the Enhanced Storage Certificate Management tool lists all the IEEE 1667-compliant USB storage devices that are connected to the computer.
ms.assetid: ae0e2991-32db-42b3-839d-83b7e2b8b35f
keywords:
- /List Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /List
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# /List Switch


The **/List** switch of the Enhanced Storage Certificate Management tool lists all the IEEE 1667-compliant USB storage devices that are connected to the computer. This switch can also be used to list the certificates (together with their properties) within the authentication silo certificate (ASC) store in a specified USB storage device.

```
    EhStorCertMgrCmd /List [-Volume:
    VolumeName
    ]
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume_______"></span><span id="_______-volume_______"></span><span id="_______-VOLUME_______"></span> **-Volume:**   
The volume name of an IEEE 1667-compliant USB storage. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.



### <span id="comments"></span><span id="COMMENTS"></span>Comments

If you use the **/List** switch without any parameters, the tool reports on all the IEEE 1667-compliant USB storage devices that are connected to the computer. In this case, only the volume names of the USB storage devices are reported.

For more information about a particular USB storage device, use the **-Volume** parameter to specify the device. In this case, the tool reports on the certificates that are present within the ASC store in the device.

### <span id="example"></span><span id="EXAMPLE"></span>Example

This example shows how to list the IEEE 1667-compliant USB storage devices that are connected to the computer.

```
EhStorCertMgrCmd /List
```

```
Executing list switch...
Volume Name : \\?\usbstor#ieee1667control&ven_msft&prod_disk_sim_v0.01&rev_0.01#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}
```

This example shows how to list the details about the certificates within the ASC store of an IEEE 1667-compliant USB storage device.

```
EhStorCertMgrCmd.exe /List -Volume:"\\?\usbstor#ieee1667control&ven_msft&prod_disk_sim_v0.01&rev_0.01#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}"
```

```
Executing List operation for specified volume name...
## Certificate Subject             : Microsoft Cert Simulator RSA 1024 SHA-1
---------------------------------
Certificate Index               : 0
Issued To                       : Microsoft Cert Simulator RSA 1024 SHA-1
Issued By                       : Microsoft 1667 Simulator Root
Certificate Expiration Date     : 12/30/9999
Certificate Status              : A certificate chain could not be built to a trusted root authority.

## Certificate Subject             : PCp PKCS SHA-1 1024 no ext
---------------------------------
Certificate Index               : 1
Issued To                       : PCp PKCS SHA-1 1024 no ext
Issued By                       : PCp PKCS SHA-1 1024 no ext
Certificate Expiration Date     : 5/31/2010
Certificate Status              : Certificate is Valid

## Certificate Subject             : HCh PKCS SHA-1 1024 no ext
---------------------------------
Certificate Index               : 2
Issued To                       : HCh PKCS SHA-1 1024 no ext
Issued By                       : HCh PKCS SHA-1 1024 no ext
Certificate Expiration Date     : 5/31/2010
Certificate Status              : Certificate is Valid
```









