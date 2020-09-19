---
title: Bug Check 0x1D4 UCMUCSI_LIVEDUMP 
description: The UCMUCSI_LIVEDUMP live dump has a value of 0x000001D4.
keywords: ["Bug Check 0x1D4 UCMUCSI_LIVEDUMP",  "UCMUCSI_LIVEDUMP"]
ms.date: 02/07/2020
topic_type:
- apiref
api_name:
- UCMUCSI_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1D4: UCMUCSI\_LIVEDUMP  

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

The UCMUCSI_LIVEDUMP live dump has a value of 0x000001D4. This indicates that the UcmUcsi class extension has encountered an error. For example this can be because a UCSI command has timed out, or because a UCSI command execution failed because the client driver returned failure.

The UcmUcsiCx.sys is the included UCSI Class Extension. For more information, see [USB Type-C Connector System Software Interface (UCSI) driver](../usbcon/ucsi.md).

## UCMUCSI\_LIVEDUMP Parameters

Parameter | Description
|---------|--------------|
1 | Type of failure - see values below
2 | The UCSI command value.
3 | If non-zero, the pointer to additional information. Use `dt UcmUcsiCx!UCMUCSICX_TRIAGE` to display.
4 | Reserved.

**Type of Failure**

0x0 : A UCSI command has timed out because the firmware did not respond to the command in time.

0x1 : A UCSI command execution failed either because the client driver returned failure or because the firmware returned an error code.

## See also

[USB Team Blog - Debugging UCSI firmware failures](https://techcommunity.microsoft.com/t5/microsoft-usb-blog/debugging-ucsi-firmware-failures/ba-p/283226)

[Universal Serial Bus (USB)](../usbcon/index.md)