package teamplay;

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("=========================================================================");
        System.out.println("|                    다음 프로그램 매뉴 중 하나를 선택하세요                   |");
        System.out.println("|   1. 입력:   학생의 데이터를 입력(학번, 성명, 국어 성적, 영어 성적, 수학 성적)   |");
        System.out.println("|   2. 개인별 출력                                                        |");
        System.out.println("|   3. 한 분반 성적 출력                                                   |");
        System.out.println("|   4. 종료                                                              |");
        System.out.println("=========================================================================");
        Scanner sc = new Scanner(System.in);
        System.out.print("학생수를 입력하세요: ");
        int student_num = sc.nextInt();
        Student[] student = new Student[student_num];

        while (true) {
            System.out.print("번호를 입력하세요 => ");
            int num = sc.nextInt();

            if (num == 1) {
                student = StudentInformation(student_num);
            }
            else if (num == 2) {
                printTestInfo(student);
            }
            else if (num == 3) {
                printClassTestInfo(student);
            }
            else if (num == 4) {
                System.out.println("프로그렘 종료");
                break;
            }
            else if (num > 4) {
                System.out.println("1~4번의 메뉴만 가능해요. 원하는 메뉴를 다시 입력하세요.");
                continue;
            }
        }
    sc.close();
    }

    public static Student[] StudentInformation(int num) {
        Student[] student = new Student[num];
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < student.length; i++) {
            System.out.print("학번을 입력하세요: ");
            int studentID = scanner.nextInt();
            System.out.print("이름을 입력하세요: ");
            String name = scanner.next();
            System.out.print("국어 성적을 입력하세요: ");
            int koreanScore = scanner.nextInt();
            System.out.print("영어 성적을 입력하세요: ");
            int englishScore = scanner.nextInt();
            System.out.print("수학 성적을 입력하세요: ");
            int mathScore = scanner.nextInt();
            student[i] = new Student(studentID, name, koreanScore, englishScore, mathScore);
        }
        return student;
    }
    
    public static void printTestInfo(Student[] student) {
        for (Student s : student) {
            System.out.println("##### " + s.getName() + " 성적표 #####");
            System.out.println("-----------------------");
            System.out.println("학번            :" + s.getStudentID());
            System.out.println("성명            :" + s.getName());
            System.out.println("-----------------------");
            System.out.println("국어            :" + s.getKoreanScore());
            System.out.println("국어 학점        :" + subjectGrade(s.getKoreanScore()));
            System.out.println("영어            :" + s.getEnglishScore());
            System.out.println("영어 학점        :" + subjectGrade(s.getEnglishScore()));
            System.out.println("수학            :" + s.getMathScore());
            System.out.println("수학 학점        :" + subjectGrade(s.getMathScore()));
            System.out.println("-----------------------");
            double average = s.gettotalScore() / student.length;
            System.out.println("총점: " + s.gettotalScore());
            System.out.println("평균: " + average);
            System.out.println("-----------------------");
        }
    }

    public static void printClassTestInfo(Student[] student) {
        System.out.println("\t ################ 학급 성적표 ################");
        System.out.println("------------------------------------------------------------------------");
        System.out.println("   학번" + " \t\t " +  "성명" + "\t" +  "국어" + " \t " + "국어학점" + "\t\t" + "영어" +
                " \t " + "영어학점" + " \t " +  "수학" + " \t " +  "수학학점" + " \t " +
                "총점" + "\t" +  "평균");
        System.out.println("------------------------------------------------------------------------");
        
        for (Student s : student) {
            System.out.println(s.getStudentID() + "\t" + s.getName() + "\t" + s.getKoreanScore() + "\t" +
                    " \t  " + subjectGrade(s.getKoreanScore()) + " \t  \t" + s.getEnglishScore() + "\t\t" +
                    subjectGrade(s.getEnglishScore()) + "\t\t\t" + s.getMathScore() + subjectGrade(s.getMathScore()));
        }
    }

    public static String getGrade(int score) {
    try {
        if (score >= 90) {
            return "A";
        } else if (score >= 80) {
            return "B";
        } else if (score >= 70) {
            return "C";
        } else if (score >= 60) {
            return "D";
        } else if (score >= 0) {
            return "F";
        } else {
            throw new IllegalArgumentException("문지가 아닌 정수로 입력하세요.");
        } catch(IllegalArgumentException e) {
            System.out.println();
            return score;
        }
    }
}
