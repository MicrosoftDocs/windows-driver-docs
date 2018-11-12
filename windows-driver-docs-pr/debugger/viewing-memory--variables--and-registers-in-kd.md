---
title: Viewing and Editing Memory in KD
description: Viewing and Editing Memory in KD
ms.assetid: 7E40F32F-C7B4-44A2-B3F9-84D673013EB2
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Viewing and Editing Memory in KD


## <span id="Viewing_and_Editing_Memory"></span><span id="viewing_and_editing_memory"></span><span id="VIEWING_AND_EDITING_MEMORY"></span>Viewing and Editing Memory


In KD, you can view and edit memory by entering one of the [**Display Memory**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) commands, and you can edit memory by entering one of the [**Enter Values**](e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-.md) commands. For a detailed discussion of these commands, see [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) and [Accessing Memory by Physical Address](accessing-memory-by-physical-address.md).

## <span id="Viewing_and_Editing_Variables"></span><span id="viewing_and_editing_variables"></span><span id="VIEWING_AND_EDITING_VARIABLES"></span>Viewing and Editing Variables


In KD, you can view and edit global variables by entering commands. The debugger interprets the name of a global variable as a virtual address. Therefore, all of the commands that are described in [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) can be used to read or write global variables. For additional information about viewing and editing global variables, see [Accessing Global Variables](accessing-global-variables.md).

In KD you can view and edit local variables by entering commands. The debugger interprets the name of a local variable as an address. Therefore, all of the commands that are described in [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) can be used to read or write local variables. However, if it is necessary to indicate to a command that a symbol is local, precede the symbol with a dollar sign ( $ ) and an exclamation point ( ! ), as in `$!var`. For additional information about viewing and editing local variables, see [Accessing Local Variables](accessing-local-variables.md).

 

 





