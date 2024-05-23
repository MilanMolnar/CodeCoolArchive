import java.io.Serializable;

public abstract class Song implements Serializable {
    private String title;
    private int length;

    public Song(){}

    public Song(String title){
        this.title = title;
    }

    public String getTitle(){
        return title;
    }

    public int getLength(){
        return length;
    }

    public void setTitle(String title){
        this.title = title;
    }

    public void setLength(int len){
        this.length = len;
    }

}
