---
title: /Remove Switch
description: The /Remove switch of the Enhanced Storage Certificate Management tool removes a specified certificate from the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device.Note  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type EhStorCertMgrCmd /List at the command prompt and then press Enter.
ms.assetid: c74fe7c3-264e-4bbd-9036-b5a254b3ba5b
keywords:
- /Remove Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /Remove
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# /Remove Switch


The **/Remove** switch of the Enhanced Storage Certificate Management tool removes a specified certificate from the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device.

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.



```
    EhStorCertMgrCmd /Remove  -Volume:
    VolumeName
     -Index:
    IndexValue
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume_______"></span><span id="_______-volume_______"></span><span id="_______-VOLUME_______"></span> **-Volume:**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.



<span id="_______-Index_______"></span><span id="_______-index_______"></span><span id="_______-INDEX_______"></span> **-Index:**   
The index within the ASC store where the certificate will be removed. The index value must be greater than one.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/Remove** switch removes all certificates from the target device except for following certificates:

-   The provisioning certificate (PCp). To remove the PCp certificate, you must use the [**/Initialize switch**](-initialize-switch.md).

-   The ASC-manufacturer certificate (ASCm).

    **Note**   The Enhanced Storage Certificate Management tool cannot add, remove, or replace the ASC-manufacturer (ASCm) certificate from the ASC store in the target device.



To remove certificates from the target device, the device must have been provisioned with a PCp certificate, and the private key of that certificate must reside in the host so that it can pass administrative authentication with the device.

If you remove an ASC-host certificate (ASCh), the tool removes all related signer certificates (SCh) in the ASCh certificate chain.

If you remove a SCh certificate from an ASCh certificate chain, the tool removes the specified SCh certificate together with its entire parent SCh certificates in the certificate chain.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to remove the certificate at index two within the ASC store of a target device:

```
EhStorCertMgrCmd /Remove -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}" -Index:2
```









