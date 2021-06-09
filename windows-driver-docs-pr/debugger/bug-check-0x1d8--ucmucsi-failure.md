---
title: Bug Check 0x1D8 UCMUCSI_FAILURE
description: The UCMUCSI_FAILURE bug check has a value of 0x000001D8. It indicates that that the UCSI class extension has encountered an error.
keywords: ["Bug Check 0x1D8 UCMUCSI_FAILURE", "UCMUCSI_FAILURE"]
ms.date: 01/11/2019
topic_type:
- apiref
api_name:
- UCMUCSI_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1D8: UCMUCSI\_FAILURE

The UCMUCSI\_FAILURE bug check has a value of 0x000001D8. It indicates that the UCSI class extension has encountered an error.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 
## UCMUCSI\_FAILURE Parameters

|Parameter|Description|
|-------- |---------- |
|1| Type of failure. VALUES: **0x0** : A UCSI command has timed out because the firmware did not respond to the command in time. **0x1** : A UCSI command execution failed either because the client driver returned failure or because the firmware returned an error code. |
|2| The UCSI command value. |
|3| If non-zero, the pointer to additional information (use `dt UcmUcsiCx!UCMUCSICX_TRIAGE`). |
|4| Reserved. |

## ## Cause

The UcmUcsi driver has encountered an error. The driver has found settings to trigger a system crash instead of a livedump.

## Resolution
-----

A UCSI Command typically fails when UCSI firmware is not responsive and UcmUcsiCx times out on a UCSI command or the UCSI firmware has indicated an error in response to a critical UCSI command sent by UcmUcsiCx.

Run `!rcdrkd.rcdrlogdump UcmUcsiCx` for more information on the cause of this failure. 

For more information on analyzing this bug check, see this blog post - [Debugging UCSI firmware failures](https://techcommunity.microsoft.com/t5/Microsoft-USB-Blog/Debugging-UCSI-firmware-failures/ba-p/283226).


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

