---
title: C28616
description: Warning C28616 Multithreaded AV condition.
ms.assetid: 77be6a23-18dc-420c-9359-ab91f216c73b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28616


warning C28616: Multithreaded AV condition

In a multithreaded environment, it is impossible to know when a thread is preempted, with the consequence that the apparent effect of reducing the reference count of an object is that it is deleted without further action on the part of the current thread. There should be no access to a reference-counted object after the reference count could potentially be at zero.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The following is an example of threading time sequence that could expose this problem:

A thread T1 executes lines 1, 2, and 3, decrements **m\_cRef** to 1, and is preempted.

Another thread T2 executes lines 1, 2, and 3 decrements **m\_cRef** to 0. Then it executes lines 4 and 5, where **this** is deleted, and finally executes line 6.

When T1 is rescheduled, it will reference **m\_cref** on line 9. Thus it will access a member variable after the related this pointer has been deleted—and when the heap for the object is in an unknown state.

```
  1 ULONG CObject::Release()
  2 {
  3     if ( 0 == InterlockedDecrement(&m_cRef) )
  4     {
  5         delete this;
  6         return NULL;
  7     }
  8     /* this.m_cRef isn&#39;t thread safe */
  9     return m_cRef;
 10 }
```

The corrected example does not reference any heap memory after the object is deleted.

```
ULONG CObject::Release()
{
 ASSERT( 0 != m_cRef );
 ULONG cRef = InterlockedDecrement(&m_cRef);
 if ( 0 == cRef )
 {
 delete this;
 }
 return cRef;
}
```

 

 





