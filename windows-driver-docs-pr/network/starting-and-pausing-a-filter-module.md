---
title: Starting and Pausing a Filter Module
description: Starting and Pausing a Filter Module
ms.assetid: 7c12846a-0934-4397-b236-487a812a01f4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting and Pausing a Filter Module





NDIS pauses a filter module to stop data flow that could interfere with Plug and Play operations, for example, adding or removing a filter module in a driver stack, or to add a new binding. For more information about how to modify a running driver stack, see [Modifying a Running Driver Stack](modifying-a-running-driver-stack.md).

NDIS starts a filter module from the *Paused* state. The filter module enters the *Paused* state after the attach operation is complete or after a pause operation is complete.

The following topics provide more information about starting and pausing a filter module:

[Starting a Filter Module](starting-a-filter-module.md)

[Pausing a Filter Module](pausing-a-filter-module.md)

 

 





