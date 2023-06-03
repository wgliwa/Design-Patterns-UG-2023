package threadlocal;

final class LocalSingleton {


    private static final ThreadLocal<LocalSingleton> threadLocal =
            ThreadLocal.withInitial(LocalSingleton::new);

    public static LocalSingleton getInstance() {
        return threadLocal.get();
    }
}