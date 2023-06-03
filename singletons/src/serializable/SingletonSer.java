package serializable;

import java.io.Serial;
import java.io.Serializable;

public class SingletonSer implements Serializable {

    private static SingletonSer instance = new SingletonSer();

    private SingletonSer() {}

    public static SingletonSer getInstance() {
        if (instance == null) {
            instance = new SingletonSer();
        }
        return instance;
    }

    @Serial
    protected Object readResolve() {
        return getInstance();
    }
}