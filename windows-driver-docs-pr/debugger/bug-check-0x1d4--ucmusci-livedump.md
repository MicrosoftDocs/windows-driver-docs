---
title: Bug Check 0x1D4 UCMUCSI_LIVEDUMP 
description: The UCMUCSI_LIVEDUMP live dump has a value of 0x000001D4.
keywords: ["Bug Check 0x1D4 UCMUCSI_LIVEDUMP",  "UCMUCSI_LIVEDUMP"]
ms.date: 02/22/2019
topic_type:
- apiref
api_name:
- UCMUCSI_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check Bug Check 0x1D4: UCMUCSI\_LIVEDUMP  

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


The UCMUCSI_LIVEDUMP live dump has a value of 0x000001D4. 

The UcmUcsi.sys driver has encountered an error. UcmUcsi.sys is an-in box USB Connector Manager UCSI client driver. For more information, see [USB Type-C Connector System Software Interface (UCSI) driver](https://docs.microsoft.com/windows-hardware/drivers/usbcon/ucsi).


## UCMUCSI\_LIVEDUMP Parameters

Parameter | Description 
|---------|--------------|
1 | Type of failure - see values below
2 | The UCSI command value.
3 | If non-zero, the pointer to additional information (dt UcmUcsiCx!UCMUCSICX_TRIAGE).
4 | Reserved.
 
**Type of Failure**

0x0 : A UCSI command has timed out because the firmware did not respond to the command in time.

0x1 : A UCSI command execution failed either because the client driver returned failure or because the firmware returned an error code.




