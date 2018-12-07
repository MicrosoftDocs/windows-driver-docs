---
title: Using a Driver-Defined Callback Object
description: Using a Driver-Defined Callback Object
ms.assetid: b3b32534-0641-4818-9384-65fd45f689e8
keywords: ["callback objects WDK kernel", "driver-defined callback objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using a Driver-Defined Callback Object





To use a callback object defined by another driver, a driver opens the object, then registers a routine to be called when the callback is triggered, as shown in the following figure. The driver requesting notification must know the name of the callback object and must understand the semantics of the arguments passed to the callback routine.

![diagram illustrating registration for callback notification](images/3reg-cbk.png)

Before it can open the object, the driver must call [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804) to create an attribute block, specifying the name of the object. After it has a pointer to an attribute block, it calls [**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560), passing the attribute pointer, a location in which to receive a handle to the callback, and **FALSE** for the *Create* parameter, indicating that it requires an existing callback object.

The driver can then call [**ExRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545534) with the returned handle to register its callback routine.

The callback routine has the following prototype:

```cpp
typedef VOID (*PCALLBACK_FUNCTION ) (
    IN PVOID CallbackContext,
    IN PVOID Argument1,
    IN PVOID Argument2
    );
```

The *CallbackContext* parameter is the context pointer to be passed to the callback routine each time it is called. Typically, this parameter is a pointer to a block of context data, which the caller should allocate from nonpaged pool if the routine can be called at DISPATCH\_LEVEL. The two arguments are defined by the component that created the callback. Typically, the arguments provide information about the conditions that triggered the callback.

When the creator of the callback triggers notification, the system calls the registered routine, passing a pointer to the context and the two arguments. Values for the arguments are supplied by the component that created the callback. The callback routine is called at the same IRQL at which the creating driver triggered notification, which is always IRQL &lt;= DISPATCH\_LEVEL.

In its callback routine, a driver can perform whatever tasks it requires for the current conditions.

When the driver no longer requires notification, it should call [**ExUnregisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545649) to remove its routine from the list of registered callbacks and to remove its reference to the callback object.

 

 




