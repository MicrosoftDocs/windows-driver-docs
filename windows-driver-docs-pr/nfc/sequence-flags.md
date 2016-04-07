---
title: Sequence flags
author: windows-driver-content
description: The NFC CX defines the following constants for sequence events.
ms.assetid: AC6CE286-52F7-4FC9-9F38-CD10C1413A90
topic_type:
- apiref
api_name:
- NFC_CX_SEQUENCE_PRE_INIT_FLAG_SKIP_CONFIG
- NFC_CX_SEQUENCE_PRE_INIT_FLAG_FORCE_CONFIG
- NFC_CX_SEQUENCE_INIT_COMPLETE_FLAG_REDO
- NFC_CX_SEQUENCE_PRE_NFCEE_DISC_FLAG_SKIP
- NFC_CX_SEQUENCE_PRE_SHUTDOWN_FLAG_SKIP_RESET
api_type:
- NA
---

# Sequence flags


The NFC CX defines the following constants for sequence events.

<a href="" id="nfc-cx-sequence-pre-init-flag-skip-config"></a>**NFC\_CX\_SEQUENCE\_PRE\_INIT\_FLAG\_SKIP\_CONFIG**
0x00000001
This flag is used in the pre-init sequence to skip configuration updates after NCI initialization. Note this flag cannot be used with force configuration option.

<a href="" id="nfc-cx-sequence-pre-init-flag-force-config"></a>**NFC\_CX\_SEQUENCE\_PRE\_INIT\_FLAG\_FORCE\_CONFIG**
0x00000002
This flag is used to force update configuration after NCI initialization. Typically, NFC CX only updates the configuration either if the controller doesn’t support KEEP CONFIG or if the configuration has changed after a driver update. The driver persists the current configuration using a session ID.

<a href="" id="nfc-cx-sequence-init-complete-flag-redo"></a>**NFC\_CX\_SEQUENCE\_INIT\_COMPLETE\_FLAG\_REDO**
0x00000001
This flag is used in init complete sequence to redo the initialization sequence. This is typically used if the client driver has performed a firmware download or updated hardware settings that require a reboot.

<a href="" id="nfc-cx-sequence-pre-nfcee-disc-flag-skip"></a>**NFC\_CX\_SEQUENCE\_PRE\_NFCEE\_DISC\_FLAG\_SKIP**
0x00000001
This flag is used during NFCEE pre-discovery sequence to skip performing the NFCEE discovery.

<a href="" id="nfc-cx-sequence-pre-shutdown-flag-skip-reset"></a>**NFC\_CX\_SEQUENCE\_PRE\_SHUTDOWN\_FLAG\_SKIP\_RESET**
0x00000001
This flag forces the NFC CX to not send an NCI reset during shutdown.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Sequence%20flags%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




