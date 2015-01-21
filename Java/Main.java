import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import javax.imageio.ImageIO;

public class Main {
static HashSet<Pixel> ensRoot;
//static long elapseTime = 0;

public static class Pixel {
int x;
int y;
Pixel pere = this;
int taille = 1;

public Pixel(int x,int y){
        this.x = x;
        this.y = y;
}
public Pixel root(){
        if(this == this.pere) return this;
        else{
                this.pere = this.pere.root();
                return this.pere;
        }
}
public void union(Pixel v){
        Pixel rootU = this.root();
        Pixel rootV = v.root();
        if (rootU != rootV) {
                if (rootU.taille > rootV.taille) {
                        rootV.pere = rootU;
                        ensRoot.remove(rootV);
                        rootU.taille += rootV.taille;
                }
                else{
                        rootU.pere = rootV;
                        ensRoot.remove(rootU);
                        rootV.taille += rootU.taille;
                }
        }
}
}


public static int dicho1(List<Pixel> valeurs,int val){
        //boolean trouve= false;
        int id=0,ifin=valeurs.size(),im=0;
        while((ifin - id) > 1) {
                im = (id + ifin)/2;
                if(valeurs.get(im).x == val) {
                        im--;
                        break;
                }
                else if(valeurs.get(im).x > val) ifin = im;
                else id = im;
        }
        return im+1;
}

public static int dicho2(List<Pixel> valeurs,int val){
        //boolean trouve= false;
        int id=0,ifin=valeurs.size(),im=0;
        while((ifin - id) > 1) {
                im = (id + ifin)/2;
                if(valeurs.get(im).x == val) {
                        im++;
                        break;
                }
                else if(valeurs.get(im).x > val) ifin = im;
                else id = im;
        }
        return im-1;
}


static public int nombreClasse(int n){
        int i = 0;
        for (Pixel element : ensRoot) {
                if (element.taille > n) i += 1;
        }
        return i;
}

public static void main(String[] args) {
        //long in2 = System.currentTimeMillis();
        int r = 0;
        try {
                r = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
                System.out.println("Erreur avec le deuxieme argument");
        }
        int n = 0;
        try {
                n = Integer.parseInt(args[2]);
        } catch (NumberFormatException e) {
                System.out.println("Erreur avec le troisieme argument");
        }
        BufferedImage bfim = null;
        try {
                bfim = ImageIO.read(new File(args[0]));
        } catch (IOException e) {
                System.out.println("Erreur avec l'ouverture de l'image!");
        }

        int width = bfim.getWidth();
        int heigth = bfim.getHeight();

        ArrayList<ArrayList<Pixel> > pixelEns = new ArrayList<ArrayList<Pixel> >();
        ensRoot = new HashSet<Pixel>();
        int yA = 0;
        int rR =  (int)Math.sqrt(r);
        int xA;
        int xxA;
        int yB;
        int xB;
        int xN;
        Pixel pix;
        while(yA < heigth) {
                //System.out.println("Coucou");
                pixelEns.add(new ArrayList<Pixel>());
                xA = 0;
                xxA = 0;
                while(xxA < width) {
                        if(bfim.getRGB(xxA,yA)!=-1) {
                                xA++;
                                pix = new Pixel(xxA, yA);
                                pixelEns.get(yA).add(pix);
                                ensRoot.add(pix);
                                yB = yA;
                                while(yB > -1) {
                                        if (yB == yA) {
                                                xB = xA - 1;
                                                //long in = System.currentTimeMillis();
                                                xN = dicho1(pixelEns.get(yB), pix.x - rR);
                                                //
                                                //elapseTime += System.currentTimeMillis() - in;
                                        }
                                        else{
                                                //long in = System.currentTimeMillis();
                                                xN = dicho1(pixelEns.get(yB), pix.x - (int)Math.sqrt(r-(yB-yA)*(yB-yA)));
                                                xB = dicho2(pixelEns.get(yB), pix.x + (int)Math.sqrt(r-(yB-yA)*(yB-yA)));
                                                //elapseTime += System.currentTimeMillis() - in;
                                        }
                                        while(xB>=xN) {
                                                pix.union(pixelEns.get(yB).get(xB));
                                                xB -= 1;
                                        }
                                        yB -= 1;
                                        if ((yA - yB) > rR)
                                                yB = -1;
                                }
                        }
                        xxA += 1;
                }
                yA += 1;
        }
        System.out.println(nombreClasse(n));
        //System.out.println(System.currentTimeMillis() - in2);
        //System.out.println(elapseTime);
}
}
