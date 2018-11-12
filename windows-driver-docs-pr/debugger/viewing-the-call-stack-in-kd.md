---
title: Viewing the Call Stack in KD
description: In KD, you can view the call stack by entering one of the k (Display Stack Backtrace) commands.
ms.assetid: 81F5D9EA-48CE-4F29-B74E-282824E690F6
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Viewing the Call Stack in KD


The call stack is the chain of function calls that have led to the current location of the program counter. The top function on the call stack is the current function, the next function is the function that called the current function, and so on. The call stack that is displayed is based on the current program counter, unless you change the register context. For more information about how to change the register context, see [Changing Contexts](changing-contexts.md).

In KD, you can view the call stack by entering one of the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands.

 

 





