---
title: METransformNeedInput
description: The METransformNeedInput event indicates that a device transform needs an input.
ms.assetid: AACD80F6-90A1-4338-AE5B-4A9248747949
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# METransformNeedInput


The **METransformNeedInput** event indicates that a device transform needs an input.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


This event is sent when a device transform needs input to generate output. Typically, async MFTs use this message to get input samples for processing and producing an output sample.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


| Parameter              | Description                                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------------------|
| **Input stream index** | The input stream index is sent in the IMFMediaEvent attribute store as **MF\_EVENT\_MFT\_INPUT\_STREAM\_ID**. |

 

## Remarks


This event will not be handled by device transform manager (DTM) for the following reasons:

-   Devproxy does not have any input pins
-   Even though Device MFT has input pins, it is automatically fed samples when they are available on the output of Devproxy. Therefore, there is no need for Device MFT to request for samples. This request would be ignored by DTM.

 

 





