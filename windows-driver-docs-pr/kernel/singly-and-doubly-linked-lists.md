---
title: Singly and Doubly Linked Lists
description: Singly and doubly linked lists
keywords: ["singly linked lists WDK kernel", "doubly linked lists WDK kernel", "sequenced singly linked lists WDK kernel", "SINGLE_LIST_ENTRY", "LIST_ENTRY"]
ms.date: 06/16/2017
ms.topic: concept-article
---

# Singly and Doubly Linked Lists

## Singly Linked Lists

The operating system provides built-in support for singly linked lists that use [**SINGLE_LIST_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-single_list_entry) structures. A singly linked list consists of a list head plus some number of list entries. (The number of list entries is zero if the list is empty.) Each list entry is represented as a **SINGLE_LIST_ENTRY** structure. The list head is also represented as a **SINGLE_LIST_ENTRY** structure.

Each **SINGLE_LIST_ENTRY** structure contains a **Next** member that points to another **SINGLE_LIST_ENTRY** structure. In the **SINGLE_LIST_ENTRY** structure that represents the list head, the **Next** member points to the first entry in the list, or is NULL if the list is empty. In the **SINGLE_LIST_ENTRY** structure that represents an entry in the list, the **Next** member points to the next entry of the list, or is NULL if this entry is the last in the list.

The routines that manipulate a singly linked list take a pointer to a [**SINGLE_LIST_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-single_list_entry) that represents the list head. They update the **Next** pointer so that it points to the first entry of the list after the operation.

Suppose that the *ListHead* variable is a pointer to the **SINGLE_LIST_ENTRY** structure that represents the list head. A driver manipulates *ListHead* as follows:

- To initialize the list as empty, set *ListHead***-&gt;Next** to be **NULL**.

- To add a new entry to the list, allocate a **SINGLE_LIST_ENTRY** to represent the new entry, and then call [**PushEntryList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pushentrylist) to add the entry to beginning of the list.

- Pop the first entry off the list by using [**PopEntryList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-popentrylist).

A **SINGLE_LIST_ENTRY**, by itself, only has a **Next** member. To store your own data in the lists, embed the **SINGLE_LIST_ENTRY** as a member of the structure that describes the list entry, as follows.

```cpp
typedef struct {
  // driver-defined members
  .
  .
  .
  SINGLE_LIST_ENTRY SingleListEntry;
 
  // other driver-defined members
  .
  .
  .
} XXX_ENTRY;
```

To add a new entry to the list, allocate an **XXX_ENTRY** structure, and then pass a pointer to the **SingleListEntry** member to
 [**PushEntryList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pushentrylist). To convert a pointer to the **SINGLE_LIST_ENTRY** back to an **XXX_ENTRY**, use [**CONTAINING_RECORD**](/windows/win32/api/ntdef/nf-ntdef-containing_record).
  Here's an example of routines that insert and remove driver-defined entries from a singly linked list.

```cpp
typedef struct {
  PVOID DriverData1;
  SINGLE_LIST_ENTRY SingleListEntry;
  ULONG DriverData2;
} XXX_ENTRY, *PXXX_ENTRY;

void
PushXxxEntry(PSINGLE_LIST_ENTRY ListHead, PXXX_ENTRY Entry)
{
    PushEntryList(ListHead, &(Entry->SingleListEntry));
}

PXXX_ENTRY
PopXxxEntry(PSINGLE_LIST_ENTRY ListHead)
{
    PSINGLE_LIST_ENTRY SingleListEntry;
    SingleListEntry = PopEntryList(ListHead);
    return CONTAINING_RECORD(SingleListEntry, XXX_ENTRY, SingleListEntry);
}
```

The system also provides atomic versions of the list operations, [**ExInterlockedPopEntryList**](/previous-versions/ff545408(v=vs.85)) and [**ExInterlockedPushEntryList**](/previous-versions/ff545418(v=vs.85)). Each takes an extra spin lock parameter. The routine acquires the spin lock before it updates the list, and then the routine releases the spin lock after the operation is completed. While the lock is held, interrupts are disabled. Each operation on the list must use the same spin lock to ensure that each such operation on the list is synchronized with every other operation. You must use the spin lock only with these **ExInterlocked*Xxx*List** routines. Don't use the spin lock for any other purpose. Drivers can use the same lock for multiple lists, but this behavior increases lock contention so drivers should avoid it.

For example, the **ExInterlockedPopEntryList** and **ExInterlockedPushEntryList** routines can support sharing of a singly linked list by a driver thread running at IRQL = PASSIVE_LEVEL and an ISR running at DIRQL. These routines disable interrupts when the spin lock is held. Thus, the ISR and driver thread can safely use the same spin lock in their calls to these **ExInterlocked*Xxx*List** routines without risking a deadlock.

Don't mix calls to the atomic and nonatomic versions of the list operations on the same list. If the atomic and nonatomic versions are run simultaneously on the same list, the data structure might become corrupted and the computer might stop responding or bug check (that is, *crash*). (You can't acquire the spin lock while calling the nonatomic routine as an alternative to mixing calls to atomic and nonatomic versions of list operations. Using the spin lock in this fashion isn't supported and might still cause list corruption.)

The system also provides an alternative implementation of atomic singly linked lists that is more efficient. For more information, see [Sequenced Singly Linked Lists](#sequenced-singly-linked-lists).

## Doubly Linked Lists

The operating system provides built-in support for doubly linked lists that use [**LIST_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-list_entry) structures. A doubly linked list consists of a list head plus some number of list entries. (The number of list entries is zero if the list is empty.) Each list entry is represented as a **LIST_ENTRY** structure. The list head is also represented as a **LIST_ENTRY** structure.

Each **LIST_ENTRY** structure contains an **Flink** member and a **Blink** member. Both members are pointers to **LIST_ENTRY** structures.

In the **LIST_ENTRY** structure that represents the list head, the **Flink** member points to the first entry in the list and the **Blink** member points to the last entry in the list. If the list is empty, then **Flink** and **Blink** of the list head point to the list head itself.

In the **LIST_ENTRY** structure that represents an entry in the list, the **Flink** member points to the next entry in the list, and the **Blink** member points to the previous entry in the list. (If the entry is the last one in the list, **Flink** points to the list head. Similarly, if the entry is the first one in the list, **Blink** points to the list head.)

While these rules might seem surprising at first glance, they allow the list insertion and removal operations to be implemented with no conditional code branches.

The routines that manipulate a doubly linked list take a pointer to a [**LIST_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-list_entry) that represents the list head. These routines update the **Flink** and **Blink** members in the list head so that these members point to the first and last entries in the resulting list.

Suppose that the *ListHead* variable is a pointer to the **LIST_ENTRY** structure that represents the list head. A driver manipulates *ListHead* as follows:

- To initialize the list as empty, use [**InitializeListHead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-initializelisthead), which initializes *ListHead***-&gt;Flink** and *ListHead***-&gt;Blink** to point to *ListHead*.

- To insert a new entry at the head of the list, allocate a **LIST_ENTRY** to represent the new entry, and then call [**InsertHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-insertheadlist) to insert the entry at the beginning of the list.

- To append a new entry to the tail of the list, allocate a **LIST_ENTRY** to represent the new entry, and then call [**InsertTailList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-inserttaillist) to insert the entry at the end of the list.

- To remove the first entry from the list, use [**RemoveHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeheadlist). This returns a pointer to the removed entry from the list, or to *ListHead* if the list is empty.

- To remove the last entry from the list, use [**RemoveTailList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removetaillist). This returns a pointer to the removed entry from the list, or to *ListHead* if the list is empty.

- To remove a specified entry from the list, use [**RemoveEntryList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeentrylist).

- To check to see if a list is empty, use [**IsListEmpty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-islistempty).

- To append a list to the tail of another list, use [**AppendTailList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-appendtaillist).

A [**LIST_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-list_entry), by itself, only has **Blink** and **Flink** members. To store your own data in the lists, embed the **LIST_ENTRY** as a member of the structure that describes the list entry, as follows.

```cpp
typedef struct {
  // driver-defined members
  .
  .
  .
  LIST_ENTRY ListEntry;
 
  // other driver-defined members.
  .
  .
  .
} XXX_ENTRY;
```

To add a new entry to a list, allocate an **XXX_ENTRY** structure, and then pass a pointer to the **ListEntry** member to **InsertHeadList** or **InsertTailList**.
 To convert a pointer to a **LIST_ENTRY** back to an **XXX_ENTRY**, use [**CONTAINING_RECORD**](/windows/win32/api/ntdef/nf-ntdef-containing_record). For an example of this technique, using singly linked lists, see Singly Linked Lists above.

The system also provides atomic versions of the list operations, [**ExInterlockedInsertHeadList**](/previous-versions/ff545397(v=vs.85)), [**ExInterlockedInsertTailList**](/previous-versions/ff545402(v=vs.85)), and [**ExInterlockedRemoveHeadList**](/previous-versions/ff545427(v=vs.85)). There's no atomic version of **RemoveTailList** or **RemoveEntryList**. Each routine takes an extra spin lock parameter. The routine acquires the spin lock before updating the list and then releases the spin lock after the operation is completed. While the lock is held, interrupts are disabled. Each operation on the list must use the same spin lock to ensure that each such operation on the list is synchronized with every other. You must use the spin lock only with these **ExInterlocked*Xxx*List** routines. Don't use the spin lock for any other purpose. Drivers can use the same lock for multiple lists, but this behavior increases lock contention so drivers should avoid it.

For example, the **ExInterlockedInsertHeadList**, **ExInterlockedInsertTailList**, and **ExInterlockedRemoveHeadList** routines can support sharing of a doubly linked list by a driver thread running at IRQL = PASSIVE_LEVEL and an ISR running at DIRQL. These routines disable interrupts when the spin lock is held. Thus, the ISR and driver thread can safely use the same spin lock in their calls to these **ExInterlocked*Xxx*List** routines without risking a deadlock.

Don't mix calls to the atomic and nonatomic versions of the list operations on the same list. If the atomic and nonatomic versions are run simultaneously on the same list, the data structure might become corrupt and the computer might stop responding or bug check (that is, *crash*). (You can't acquire the spin lock while calling the nonatomic routine to avoid mixing calls to atomic and nonatomic versions of the list operations. Using the spin lock in this fashion isn't supported and might still cause list corruption.)

### Sequenced Singly Linked Lists

A sequenced singly linked list is an implementation of singly linked lists that supports atomic operations. It's more efficient for atomic operations than the implementation of singly linked lists described in [Singly Linked Lists](#singly-linked-lists).

An [**SLIST_HEADER**](./eprocess.md) structure is used to describe the head of a sequenced singly linked list, while [**SLIST_ENTRY**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_slist_entry) is used to describe an entry in the list.

A driver manipulates the list as follows:

- To initialize an **SLIST_HEADER** structure, use [**ExInitializeSListHead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-initializeslisthead).

- To add a new entry to the list, allocate a **SLIST_ENTRY** to represent the new entry, and then call [**ExInterlockedPushEntrySList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinterlockedpushentryslist) to add the entry to the beginning of the list.

- Pop the first entry off the list by using [**ExInterlockedPopEntrySList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinterlockedpopentryslist).

- To clear the list completely, use [**ExInterlockedFlushSList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinterlockedflushslist).

- To determine the number of entries in the list, use [**ExQueryDepthSList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exquerydepthslist).

A [**SLIST_ENTRY**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_slist_entry), by itself, only has a **Next** member. To store your own data in the lists, embed the **SLIST_ENTRY** as a member of the structure that describes the list entry, as follows.

```cpp
typedef struct 
{
  // driver-defined members
  .
  .
  .
  SLIST_ENTRY SListEntry;
  // other driver-defined members
  .
  .
  .

} XXX_ENTRY;
```

To add a new entry to the list, allocate an **XXX_ENTRY** structure, and then pass a pointer to the **SListEntry** member to **ExInterlockedPushEntrySList**.

To convert a pointer to the **SLIST_ENTRY** back to an **XXX_ENTRY**, use [**CONTAINING_RECORD**](/windows/win32/api/ntdef/nf-ntdef-containing_record). For an example of this technique, using nonsequenced singly linked lists, see [Singly Linked Lists](#singly-linked-lists).

**Warning**   For 64-bit Microsoft Windows operating systems, [**SLIST_ENTRY**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_slist_entry) structures must be 16-byte aligned.
