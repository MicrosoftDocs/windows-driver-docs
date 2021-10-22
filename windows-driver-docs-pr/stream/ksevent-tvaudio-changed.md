---
title: KSEVENT_TVAUDIO_CHANGED
description: The KSEVENT_TVAUDIO_CHANGED event propagates an action, such as a newly tuned-to channel supports stereo audio, from the kernel-mode video capture minidriver to DirectShow in user-mode.
keywords: ["KSEVENT_TVAUDIO_CHANGED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_TVAUDIO_CHANGED
api_type:
- NA
ms.date: 10/11/2021
ms.localizationpriority: medium
---

# KSEVENT_TVAUDIO_CHANGED

The **KSEVENT_TVAUDIO_CHANGED** event propagates an action, such as a newly tuned-to channel supports stereo audio, from the kernel-mode video capture minidriver to DirectShow in user-mode.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).
