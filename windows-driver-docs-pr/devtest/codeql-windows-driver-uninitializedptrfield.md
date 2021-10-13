---
title: UninitializedPtrField (Supplemental Windows Driver CodeQL Query)
description: UninitializedPtrField a Supplemental Windows Driver CodeQL Query
ms.date: 01/11/2021
ms.localizationpriority: medium
---

# UninitializedPtrField (Windows Driver CodeQL Query)

## Overview

A pointer field which was not initialized during or since class construction will cause a null pointer dereference.

## Recommendation

Make sure to initialize all pointer fields before usage.

## Example

The following example shows a scenario where the field *ptr_* is not initialzied and later dereferenced:

```cpp
template <typename T>
class ComPtr
{
public:
	T* ptr_;
	ComPtr() throw() : ptr_(nullptr)
	{
	}
	ComPtr(T* ptr) throw() : ptr_(ptr)
	{
	}
	T* operator->() const throw()
	{
		return ptr_;
	}
	void set(T* ptr) {
		ptr_ = ptr;
	}
	T** addr() {
		return &ptr_;
	}
};

class Test
{
public:
	int it_;
	int it() {
		return it_;
	}
};
void test() {
	Test t;
	int val;
	ComPtr<Test> ptr;
	// BAD: pointer is not initialized here
	val = ptr->it();
}
```

To correct the problem, we set the field before usage:

```cpp
template <typename T>
class ComPtr
{
public:
	T* ptr_;
	ComPtr() throw() : ptr_(nullptr)
	{
	}
	ComPtr(T* ptr) throw() : ptr_(ptr)
	{
	}
	T* operator->() const throw()
	{
		return ptr_;
	}
	void set(T* ptr) {
		ptr_ = ptr;
	}
	T** addr() {
		return &ptr_;
	}
};
class Test
{
public:
	int it_;
	int it() {
		return it_;
	}
};
void test() {
	Test t;
	int val;
	ComPtr<Test> ptr2(&t);
	// GOOD: pointer was initialized
	val = ptr2->it();
	ComPtr<Test> ptr3;
	ptr3.set(&t);
	// GOOD: pointer was set in between
	val = ptr3->it();
}
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
