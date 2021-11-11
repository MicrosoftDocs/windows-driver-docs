---
title: KSEVENT_VIDCAPTOSTI_EXT_TRIGGER
description: The KSEVENT_VIDCAPTOSTI_EXT_TRIGGER event propagates an action, such as a when a trigger button is pressed on a video capture device, from the kernel-mode video capture minidriver to DirectShow in user-mode.
keywords: ["KSEVENT_VIDCAPTOSTI_EXT_TRIGGER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDCAPTOSTI_EXT_TRIGGER
api_type:
- NA
ms.date: 10/11/2021
ms.localizationpriority: medium
---

# KSEVENT_VIDCAPTOSTI_EXT_TRIGGER

The **KSEVENT_VIDCAPTOSTI_EXT_TRIGGER** event propagates an action, such as a when a trigger button is pressed on a video capture device, from the kernel-mode video capture minidriver to DirectShow in user-mode.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).
