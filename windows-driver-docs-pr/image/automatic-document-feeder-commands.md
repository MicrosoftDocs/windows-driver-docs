---
title: Automatic Document Feeder Commands
description: Automatic Document Feeder Commands
ms.date: 03/27/2023
---

# Automatic Document Feeder Commands

The commands in this section are for microdrivers that support an automatic document feeder (ADF). To report that your microdriver supports an automatic document feeder, set the **ADF** member in the [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure to 1 (or 2 if the ADF has a duplexer) during the CMD_INITIALIZE command. This will cause the WIA Flatbed driver to add the needed properties for ADF control and use the commands in this section.

## CMD_LOAD_ADF  

Called by the WIA Flatbed driver to load a page into the ADF. If this command does not apply to the device, return E_NOTIMPL. This command is optional for a device that automatically feeds a page.

## CMD_UNLOAD_ADF  

Called by the WIA Flatbed driver to unload a page from the ADF. If this command does not apply to the device, return E_NOTIMPL. This command is optional for a device that automatically unfeeds a page.

## CMD_GETADFAVAILABLE  

Called by the WIA Flatbed driver to determine whether an ADF is available for use. If an ADF is available, return S_OK. If this command does not apply to the device, return E_NOTIMPL.

## CMD_GETADFHASPAPER  

Called by the WIA Flatbed driver to get the paper status of the device's ADF. Set the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure to the appropriate status value. (See CMD_ADFGETSTATUS for possible status values.)

## CMD_GETADFOPEN  

Same as CMD_GETADFREADY. This command is not currently used by the WIA Flatbed Driver.

## CMD_GETADFSTATUS  

Called by the WIA Flatbed driver to get the status of the ADF attached to the device. Set the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure to the appropriate status value. Possible status values are as follows.

| Status | Meaning |
|--|--|
| MCRO_ERROR_GENERAL_ERROR | General error |
| MCRO_ERROR_OFFLINE | The ADF or device is offline |
| MCRO_ERROR_PAPER_EMPTY | he ADF has no paper |
| MCRO_ERROR_PAPER_JAM | The ADF has a paper jam |
| MCRO_ERROR_PAPER_PROBLEM | The ADF has a paper problem |
| MCRO_ERROR_USER_INTERVENTION | The user needs to interact with the device |
| MCRO_STATUS_OK | There is no error to report |

## CMD_GETADFUNLOADREADY  

Called by the WIA Flatbed Driver to determine whether the ADF is ready for a page to be unloaded. If so, return S_OK. If this command does not apply to the device, return E_NOTIMPL.
