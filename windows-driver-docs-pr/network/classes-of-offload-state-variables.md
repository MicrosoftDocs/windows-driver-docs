---
title: Classes of Offload State Variables
description: Classes of Offload State Variables
ms.assetid: f4580eea-354c-4e24-861a-400a76e289f5
keywords:
- offload state WDK TCP chimney offload , variable classes
- constant variables WDK TCP chimney offload
- cached variables WDK TCP chimney offload
- delegated variables WDK TCP chimney offload
- variables WDK TCP chimney offload state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Classes of Offload State Variables


\[The TCP chimney offload feature is deprecated and should not be used.\]




There are three classes of offload state variables:

<a href="" id="constant"></a>Constant  
The value of a constant variable does not change during the life of a TCP connection. Neither the host stack nor the offload target changes the value of a constant variable. When the host stack terminates the offload of one or more state objects by causing NDIS to call the offload target's [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function, the offload target does not return the value of an offloaded constant variable to the host stack.

<a href="" id="cached"></a>Cached  
A cached variable is owned and maintained by the host stack. An offload target must not change the value of a cached variable unless this value is updated by the host stack. If the value of a cached variable changes, the host stack requests an update of the variable, which causes NDIS to call the offload target's [**MiniportUpdateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff560463) function. When the host stack terminates the offload of one or more state objects by causing NDIS to call the offload target's [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function, the offload target does not return the value of offloaded cached variables to the host stack.

<a href="" id="delegated"></a>Delegated  
The host stack provides initial values for delegated variables when it offloads such variables to the offload target. After delegated variables are offloaded, the offload target owns and maintains them. Only the offload target can change the value of an offloaded delegated variable. The offload target does not notify the host stack of changes to the values of offloaded delegated variables. However, the host stack can query the value of offloaded delegated variables, which causes NDIS to call the offload target's [**MiniportQueryOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559423) function. When the host stack terminates the offload of one or more state objects by causing NDIS to call the offload target's [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function, the offload target passes the value of delegated variables in the terminated state object back to the host stack.

For a complete listing of the offload variables for each layer of offload state, see [Offload State Objects](offload-state-objects.md).

 

 





