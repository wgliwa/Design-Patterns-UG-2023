package threadsafe;

public class SingletonThreadSafe {

    private static SingletonThreadSafe instance;

    private SingletonThreadSafe(){}

    public static SingletonThreadSafe getInstance(){
        if(instance == null){
            synchronized (SingletonThreadSafe.class) {
                instance = new SingletonThreadSafe();
            }
        }
        return instance;
    }
}