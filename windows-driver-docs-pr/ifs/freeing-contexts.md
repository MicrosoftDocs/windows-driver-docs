---
title: Freeing Contexts
description: Freeing Contexts
keywords:
- contexts WDK file system minifilter , freeing
- freeing contexts
ms.date: 01/22/2021
ms.localizationpriority: medium
---

# Freeing Contexts

A context is freed after it is [deleted](deleting-contexts.md) and all outstanding references to it have been [released](releasing-contexts.md).

There is one exception to this rule: if a context has been [created](creating-contexts.md) but has not been [set](setting-contexts.md), it does not need to be deleted. It is freed when its reference count reaches zero. See the code example in [Releasing Contexts](releasing-contexts.md).

When a minifilter [registers its context types](registering-context-types.md), each context definition can optionally include a context cleanup callback routine to be called before the context is freed. For more information, see [**PFLT_CONTEXT_CLEANUP_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_cleanup_callback).
