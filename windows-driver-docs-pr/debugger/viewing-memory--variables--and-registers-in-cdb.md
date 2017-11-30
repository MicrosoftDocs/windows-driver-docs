---
title: Viewing and Editing Memory in CDB
description: Viewing and Editing Memory in CDB
ms.assetid: EE2424F3-A692-4AEA-9F09-337C5758D8AD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Viewing and Editing Memory in CDB


## <span id="Viewing_and_Editing_Memory"></span><span id="viewing_and_editing_memory"></span><span id="VIEWING_AND_EDITING_MEMORY"></span>Viewing and Editing Memory


In CDB, you can view and edit memory by entering one of the [**Display Memory**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) commands, and you can edit memory by entering one of the [**Enter Values**](e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-.md) commands. For a detailed discussion of these commands, see [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) and [Accessing Memory by Physical Address](accessing-memory-by-physical-address.md).

## <span id="Viewing_and_Editing_Variables"></span><span id="viewing_and_editing_variables"></span><span id="VIEWING_AND_EDITING_VARIABLES"></span>Viewing and Editing Variables


In CDB, you can view and edit global variables by entering commands. The debugger interprets the name of a global variable as a virtual address. Therefore, all of the commands that are described in [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) can be used to read or write global variables. For additional information about viewing and editing global variables, see [Accessing Global Variables](accessing-global-variables.md).

In CDB you can view and edit local variables by entering commands. The debugger interprets the name of a local variable as an address. Therefore, all of the commands that are described in [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) can be used to read or write local variables. However, if it is necessary to indicate to a command that a symbol is local, precede the symbol with a dollar sign ( $ ) and an exclamation point ( ! ), as in `$!var`. For additional information about viewing and editing local variables, see [Accessing Local Variables](accessing-local-variables.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Viewing%20and%20Editing%20Memory%20in%20CDB%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




