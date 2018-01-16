import weka.classifiers.Classifier;
import weka.core.*;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] argv) {
        ObjectInputStream ois;
        Classifier classifier;

        String wekaModelPath = "./weka_models/extended dataset/";
        switch (argv[1]){
            case "bayes_net":
                wekaModelPath += "key_bayes_net.model";
                break;
            case "kstar":
                wekaModelPath += "key_kstar.model";
                break;
            case "multilayer_perceptron":
                wekaModelPath += "key_multilayer_perceptron.model";
                break;
            case "simple_logistic":
                wekaModelPath += "key_simple_logistic.model";
                break;
            case "smo":
                wekaModelPath += "key_smo.model";
                break;
            default:
                System.out.println("invalid model parameter");
                return;
        }

        try {
            classifier = (Classifier) new ObjectInputStream(new FileInputStream(wekaModelPath)).readObject();
        } catch (IOException e) {
            System.out.println("weka model file not found");
            return;
        } catch (ClassNotFoundException e) {
            System.out.println("error deserializing weka model file");
            return;
        }
        ArrayList<Attribute> attributes = new ArrayList<>();
        ArrayList<String> classValues = new ArrayList<>();

        classValues.add("G major");
        classValues.add("D major");
        classValues.add("B minor");
        classValues.add("E flat major");
        classValues.add("C major");
        classValues.add("E minor");
        classValues.add("C minor");
        classValues.add("D minor");
        classValues.add("A minor");
        classValues.add("F minor");
        classValues.add("F major");
        classValues.add("A major");
        classValues.add("G minor");
        classValues.add("E major");
        classValues.add("B flat major");
        classValues.add("C sharp major");
        classValues.add("C sharp minor");
        classValues.add("F sharp major");
        classValues.add("F sharp minor");
        classValues.add("A flat major");
        classValues.add("G sharp minor");
        classValues.add("B flat minor");
        classValues.add("B major");
        classValues.add("D sharp minor");

        attributes.add(new Attribute("C"));
        attributes.add(new Attribute("C sharp"));
        attributes.add(new Attribute("D"));
        attributes.add(new Attribute("D sharp"));
        attributes.add(new Attribute("E"));
        attributes.add(new Attribute("F"));
        attributes.add(new Attribute("F sharp"));
        attributes.add(new Attribute("G"));
        attributes.add(new Attribute("G sharp"));
        attributes.add(new Attribute("A"));
        attributes.add(new Attribute("A sharp"));
        attributes.add(new Attribute("B"));
        attributes.add(new Attribute("key", classValues));

        Instances dataset = new Instances("testdata", attributes, 1);
        dataset.setClassIndex(attributes.size() - 1);

        try {
            Runtime.getRuntime().exec("Midicsv.exe " + argv[0] + " temp.csv").waitFor();
        } catch (IOException | InterruptedException e) {
            System.out.println("Error converting MIDI file to CSV");
            return;
        }

        try {
            Runtime.getRuntime().exec("py csv_to_note_weights.py temp.csv temp.txt").waitFor();
        } catch (IOException | InterruptedException e) {
            System.out.println("Error running python script");
        }

        double[] values = new double[13];
        int index = 0;
        Scanner scanner;
        File weightsFile = new File("./temp.txt");
        try {
            scanner = new Scanner(weightsFile);
            while(scanner.hasNextDouble())
                values[index++] = scanner.nextDouble();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        File csvFile = new File("./temp.csv");

        weightsFile.delete();
        csvFile.delete();

        Instance unlabeledInstance = new DenseInstance(1.0, values);
        unlabeledInstance.setDataset(dataset);

        try {
            double classifyResult = classifier.classifyInstance(unlabeledInstance);
            System.out.println(argv[0] + " is in " + dataset.classAttribute().value((int)classifyResult));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
