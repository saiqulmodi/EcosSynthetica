import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

QUESTIONS = [
    (
        "BIO_12_GEN_001",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "Gregor Mendel conducted hybridization experiments on garden peas (Pisum sativum) for how many years?",
        "5 years (1850-1855)",
        "7 years (1856-1863)",
        "10 years (1860-1870)",
        "14 years (1870-1884)",
        1,
        "Gregor Mendel conducted hybridization experiments on garden peas for 7 years (1856-1863) and proposed the laws of inheritance in living organisms.",
        1
    ),
    (
        "BIO_12_GEN_002",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "How many pairs of contrasting characters in pea plants were selected and studied by Mendel?",
        "4 pairs",
        "7 pairs (14 true-breeding varieties)",
        "12 pairs",
        "14 pairs",
        1,
        "Mendel selected 14 true-breeding pea plant varieties as pairs which were similar except for one character with contrasting traits (7 pairs).",
        1
    ),
    (
        "BIO_12_GEN_003",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "In a monohybrid cross between heterozygous tall pea plants (Tt x Tt), what is the expected genotypic ratio among the offspring?",
        "3 : 1",
        "1 : 2 : 1",
        "9 : 3 : 3 : 1",
        "1 : 1 : 1 : 1",
        1,
        "The monohybrid phenotypic ratio is 3:1 (Tall:Dwarf), but the genotypic ratio is 1 TT : 2 Tt : 1 tt (1:2:1).",
        1
    ),
    (
        "BIO_12_GEN_004",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "What type of cross is used to determine whether a dominant phenotype individual is homozygous dominant or heterozygous?",
        "Reciprocal cross",
        "Back cross to dominant parent",
        "Test cross (crossing with homozygous recessive)",
        "Dihybrid selfing",
        2,
        "In a test cross, an organism showing a dominant phenotype is crossed with the homozygous recessive parent instead of self-crossing to determine its genotype.",
        2
    ),
    (
        "BIO_12_GEN_005",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "In Antirrhinum (snapdragon), a cross between red-flowered (RR) and white-flowered (rr) plants produces pink-flowered (Rr) progeny. This exemplifies:",
        "Codominance",
        "Incomplete dominance",
        "Complete dominance",
        "Polygenic inheritance",
        1,
        "Incomplete dominance occurs when the heterozygote displays an intermediate phenotype between the two homozygous phenotypes, yielding a 1:2:1 phenotypic and genotypic ratio in F2.",
        2
    ),
    (
        "BIO_12_GEN_006",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "Human ABO blood group inheritance is governed by gene I with alleles Iᴬ, Iᴮ, and i. This illustrates both:",
        "Incomplete dominance and pleiotropy",
        "Multiple allelism and codominance",
        "Polygenic inheritance and epistasis",
        "Sex-linked inheritance and dominance",
        1,
        "Gene I has three alleles (multiple allelism in the population), and when Iᴬ and Iᴮ are present together in an individual, both express their sugars equally (codominance).",
        2
    ),
    (
        "BIO_12_GEN_007",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "Who formulated the Chromosomal Theory of Inheritance by uniting Mendel's principles with chromosomal behavior during cell division?",
        "Watson and Crick",
        "Walter Sutton and Theodore Boveri",
        "Thomas Hunt Morgan",
        "Alfred Sturtevant",
        1,
        "Walter Sutton and Theodore Boveri (1902) noted that the behavior of chromosomes was parallel to the behavior of genes and used chromosome movement to explain Mendel's laws.",
        2
    ),
    (
        "BIO_12_GEN_008",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "Why did Thomas Hunt Morgan choose the fruit fly (Drosophila melanogaster) for his experimental verification of chromosomal theory?",
        "They have a long life cycle of several months",
        "A single mating produces few offspring",
        "They can be grown on simple synthetic medium and have clear sex dimorphism",
        "They have 46 pairs of chromosomes",
        2,
        "Drosophila completes its life cycle in about two weeks, produces large numbers of progeny per mating, can be reared on simple synthetic medium, and shows distinct morphological differences between sexes.",
        2
    ),
    (
        "BIO_12_GEN_009",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "mcq_fact",
        "In humans, phenylketonuria (PKU) is an inborn error of metabolism caused by a mutation in the gene encoding which enzyme?",
        "Tyrosinase",
        "Phenylalanine hydroxylase",
        "Homogentisate oxidase",
        "Hexosaminidase A",
        1,
        "PKU is an autosomal recessive disorder caused by the lack of phenylalanine hydroxylase, which normally converts phenylalanine into tyrosine, leading to phenylalanine accumulation and mental retardation.",
        3
    ),
    (
        "BIO_12_GEN_010",
        "bio_12_principles_of_inheritance",
        "Biology",
        12,
        "assertion_reason",
        "Statement I: Down's syndrome is caused by the presence of an additional copy of chromosome 21 (Trisomy 21).\nStatement II: Affected individuals typically show short stature, furrowed tongue, and characteristic broad palm with a single crease.",
        "Both Statement I and Statement II are correct",
        "Both Statement I and Statement II are incorrect",
        "Statement I is correct, but Statement II is incorrect",
        "Statement I is incorrect, but Statement II is correct",
        0,
        "Both statements are correct. First described by Langdon Down in 1866, Down's syndrome is an aneuploidy (trisomy 21) characterized by short stature, small round head, furrowed tongue, partially open mouth, and broad palmar crease.",
        2
    )
]

def ingest():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executemany("""
    INSERT OR REPLACE INTO questions 
    (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, QUESTIONS)

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM questions WHERE chapter_key = 'bio_12_principles_of_inheritance';")
    count = cur.fetchone()[0]
    conn.close()
    print(f"Ingested {len(QUESTIONS)} questions. Total in bio_12_principles_of_inheritance: {count}")

if __name__ == "__main__":
    ingest()