---
title: C28616 warning
description: Warning C28616 Multithreaded AV condition.
ms.date: 09/19/2022
f1_keywords: ["C28616", "INTERLOCKEDDECREMENT_MISUSE1", "__WARNING_INTERLOCKEDDECREMENT_MISUSE1"]
---
# Warning C28616

> Multithreaded AV condition

This warning indicates that a thread has potential to access deleted objects if preempted.

## Remarks

There should be no access to a reference-counted object after the reference count is at zero.

Code analysis name: INTERLOCKEDDECREMENT_MISUSE1

## Example

The following code generates this warning. This is an example of threading time sequence that could expose this problem. In this example, `m_cRef` is a member of `this`:

A thread T1 executes the `if` condition, decrements `m_cRef` to 1, and is then preempted.

Another thread T2 executes the `if` condition, decrements `m_cRef` to 0, executes the `if` body (where `this` is deleted), and returns `NULL`.

When T1 is rescheduled, it will reference `m_cref` on line 9. Thus it will access a member variable after the related `this` pointer has been deleted—and when the heap for the object is in an unknown state.

```cpp
ULONG CObject::Release()
{
    if (0 == InterlockedDecrement(&m_cRef))
    {
        delete this;
        return NULL;
    }
    /* this.m_cRef isn't thread safe */
    return m_cRef;
}
```

The following code does not reference any heap memory after the object is deleted.

```cpp
ULONG CObject::Release()
{
    ASSERT(0 != m_cRef);
    ULONG cRef = InterlockedDecrement(&m_cRef);
    if (0 == cRef)
    {
        delete this;
        return NULL;
    }
    return cRef;
}
```

 

 





