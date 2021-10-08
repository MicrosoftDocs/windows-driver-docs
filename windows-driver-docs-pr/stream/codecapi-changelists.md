---
title: CODECAPI_CHANGELISTS
description: The CODECAPI_CHANGELISTS event is used to return a list of GUIDs that have changed.
ms.date: 10/08/2021
ms.localizationpriority: medium
---

# CODECAPI_CHANGELISTS

The CODECAPI_CHANGELISTS event is used to return a list of GUIDs that have changed as a result of a property "set" call, such as [CODECAPI_ALLSETTINGS](codecapi-allsettings.md) and [CODECAPI_SETALLDEFAULTS](codecapi-setalldefaults.md), or an encoder setting property.

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| Yes (query supported) | Yes | Filter | [**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).

The driver uses the AVStream [**KsGenerateEvents**](/windows-hardware/drivers/ddi/ks/nf-ks-ksgenerateevents) to post a list of GUIDs that changed.

## See also

[**KsGenerateEvents**](/windows-hardware/drivers/ddi/ks/nf-ks-ksgenerateevents)

[CODECAPI_ALLSETTINGS](codecapi-allsettings.md)

[CODECAPI_SETALLDEFAULTS](codecapi-setalldefaults.md)
