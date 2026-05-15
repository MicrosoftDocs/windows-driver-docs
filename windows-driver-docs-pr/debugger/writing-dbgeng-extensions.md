---
title: Writing DbgEng Extensions
description: Writing DbgEng Extensions
keywords: DbgEng Extensions, debugger extensions 
ms.date: 01/05/2026
ms.topic: concept-article
---

# Writing DbgEng Extensions

DbgEng extensions are specialized DLLs that extend the Windows debugger engine's functionality by implementing custom debugging commands and callback functions. Extension code can use both the C++ interfaces from `dbgeng.h` and C functions from `wdbgexts.h`.

For more information, see these articles in the DbgEng Extension Design Guide:

- [Anatomy of a DbgEng Extension DLL](anatomy-of-a-dbgeng-extension-dll.md)
- [Using Clients and the Engine](using-clients-and-the-engine.md)
- [Writing DbgEng Extension Code](writing-dbgeng-extension-code.md)
- [Building DbgEng Extensions](building-dbgeng-extensions.md)

For the complete `dbgeng.h` reference, see [DbgEng Extension Reference](/windows-hardware/drivers/ddi/dbgeng/).

 

