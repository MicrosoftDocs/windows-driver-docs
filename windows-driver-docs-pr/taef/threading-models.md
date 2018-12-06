---
title: Threading Models
description: Threading Models
ms.assetid: 3BB0C01B-D82B-45dd-8AC8-EA2E2811CD24
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Threading Models


TAEF provides functionality for pre-configuring a COM threading model for the environment where you test execute. By default, Managed ©\#) and Script tests run on STA thread; for Native, threading model is not pre-configured.

The "ThreadingModel" metadata property is used to request a threading model. The supported values for this property are:

| Property Value | Description                                                                               |
|----------------|-------------------------------------------------------------------------------------------|
| STA            | Single-Threaded Apartment (CoInitializeEx is called with COINIT\_APARTMENTTHREADED flag). |
| MTA            | Multithreaded Apartment (CoInitializeEx is called with COINIT\_MULTITHREADED flag).       |
| None           | Threading model is not specified.                                                         |

 

## <span id="Configuring_a_threading_model"></span><span id="configuring_a_threading_model"></span><span id="CONFIGURING_A_THREADING_MODEL"></span>Configuring a threading model


Example: To request MTA threading model from C++ mark-up:

```cpp
class ThreadModelTests
{

    TEST_CLASS(ThreadModelTests);

    BEGIN_TEST_METHOD(MTAThreadingModelTest)
        TEST_METHOD_PROPERTY(L"ThreadingModel", L"STA")
    END_TEST_METHOD()
};
```

You can also request threading model property for a class or a module. For example,

```cpp
class ThreadModelTestsWithMTADefault
{

    BEGIN_TEST_CLASS(ThreadModelTestsWithMTADefault)
        TEST_CLASS_PROPERTY(L"ThreadingModel", L"Mta")
    END_TEST_CLASS()

    TEST_METHOD(DefaultWithMTASetByClass);
};
```

Similarly, you can also request threading model for managed tests:

```cpp
[TestClass]

public class SimpleTests
{
    [TestMethod]
    [TestProperty("ThreadingModel", "MTA")]
    public void Test1()
    {
        Verify.IsTrue(true);
    }

    [TestMethod]
    [TestProperty("ThreadingModel", "STA")]
    public void Test2()
    {
        Verify.IsTrue(true);
    }

    [TestMethod]
    [TestProperty("ThreadingModel", "{STA; MTA}")]
    public void SetsOfMetadataTest()
    {
        Log.Comment("In CSharpThreadingModelExample.SetsOfMetadataTest");
        DisplayAppartmentState();
    }
}
```

Notice in the last test above: SetsOfMetadataTest, it is also possible to make use of metadata sets and run the same test: first with STA threading model and then with MTA.

 

 





