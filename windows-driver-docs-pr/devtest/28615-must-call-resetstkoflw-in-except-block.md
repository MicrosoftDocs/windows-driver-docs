---
title: C28615
description: Warning C28615 Must call _resetstkoflw in the __except() block when calling _alloca in the __try block. Don't call _resetstkoflw from inside a catch() block.
ms.assetid: bccfc846-58b9-4c20-bbe7-383ecf836165
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28615


warning C28615: Must call \_resetstkoflw in the \_\_except() block when calling \_alloca in the \_\_try block. Don't call \_resetstkoflw from inside a catch() block

The Code Analysis tool reports this warning when applications call the **\_resetstkoflw** function within a catch block, or when applications call **alloca** in the try block without calling **\_resetstkoflw** in the except block.

A thread can catch only one stack overflow exception (raised from a call to **\_alloca**) unless the stack is repaired (for example, by **\_resetstkoflw**) after each exception. If the stack is not fixed after the first exception is raised from **\_alloca**, a second exception will result in immediate and silent process termination.

You must call **\_resetstkoflw** when the current stack pointer points into an address higher than the third page on the stack. This is because it doesn't make sense to make a guard page out of the current page that the stack pointer is pointing to (or will point to in a moment).

The **\_resetstkoflw** function should not be called from a structured exception handler filter expression, or from a function called from a structured exception handler filter expression.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The Code Analysis tool reports this warning for the following example because the filter expression is called before the stack unwind occurs. When there is a stack overflow, the filter expression is called when the current stack pointer is pointing to the third page from the bottom of the stack.

```
__try 
{
    /* The following could cause stack overflow */
    char *x = _alloca (i);
}
__except ((GetExceptionCode () == EXCEPTION_STACK_OVERFLOW) 
    ? (_resetstkoflw (), EXCEPTION_EXECUTE_HANDLER) 
    : EXCEPTION_CONTINUE_SEARCH)
{
}
```

The following example also fails for similar reasons.

```

__try 
{
 char *x = _alloca (i);
}
__except (SEHFilter (GetExceptionCode ()))
{
}

int SEHFilter (DWORD dwExceptionCode)
{
 if (dwExceptionCode == EXCEPTION_STACK_OVERFLOW)
 {
 _resetstkoflw ();
 return EXCEPTION_EXECUTE_HANDLER;
 }
 else
 {
 return EXCEPTION_CONTINUE_SEARCH;
 }
}
```

The following example successfully avoids the error.

```
__try
{
    char *x = _alloca (i);
}
__except ((GetExceptionCode () == EXCEPTION_STACK_OVERFLOW) ? EXCEPTION_EXECUTE_HANDLER : EXCEPTION_CONTINUE_SEARCH)
{
    // In this block the stack has already been unwound,
    // so this call will succeed.
_resetstkoflw ();
}
```









