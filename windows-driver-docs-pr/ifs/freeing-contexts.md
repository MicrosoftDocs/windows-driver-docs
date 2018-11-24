---
title: Freeing Contexts
description: Freeing Contexts
ms.assetid: e2b87662-c1bd-45a7-82a3-29817f7692fc
keywords:
- contexts WDK file system minifilter , freeing
- freeing contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Freeing Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


A context is freed after it is deleted and all outstanding references to it have been released.

There is one exception to this rule: if a context has been created but has not been set by calling **FltSet***Xxx***Context**, it does not need to be deleted. It is freed when its reference count reaches zero. (See the code example in [Releasing Contexts](releasing-contexts.md).)

When a minifilter driver registers its context types, each context definition can optionally include a context cleanup callback routine to be called before the context is freed. For more information, see [**PFLT\_CONTEXT\_CLEANUP\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551078).

 

 




