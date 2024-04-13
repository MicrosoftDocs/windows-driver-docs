---
title: IPrintOemCommon COM Interface
description: IPrintOemCommon COM Interface
ms.date: 07/14/2023
---

# IPrintOemCommon COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemCommon` COM interface enables a plug-in to specify or get device information. This interface provides functionality that is common between the user interface and rendering plug-ins.

The following table lists and describes all the methods that the `IPrintOemCommon` interface defines.

| Method | Description |
|--|--|
| **IPrintOemCommon::DevMode** | Performs operations on private DEVMODEW members. |
| **IPrintOemCommon::GetInfo** | Returns a plug-in's identification information. |

For information about how these methods are implemented for UI plug-ins, see [IPrintOemUI COM Interface](iprintoemui-com-interface.md).
