---
title: C28616
description: Warning C28616 Multithreaded AV condition.
ms.assetid: 77be6a23-18dc-420c-9359-ab91f216c73b
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28616%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




