Read Me
1.	יצירת עמודי HTML:
יצרנו את עמודי הHTML שלנו בהתאם למסכים שעיצבנו בחלק א' של הפרויקט. הוספנו header וגם footer אחידים לכל העמודים על מנת ליצור מבנה אחיד לאתר.
2.	יצרנו קובץ css בשםstyles . מטרת הקובץ היא ליצור עיצוב אחיד לכל עמודי האתר. העיצוב מתמקד ביצירת המסכים שהודגמו בחלק א' ושילוב עקרונות העיצוב שדוברו בו, עיצוב פשוט ומודרני, שימוש בצבעים כמו שחור לבן ואפור על מנת ליצור יוקרה ופשטות.
3.	במימוש הJS יצרנו קובץ בשם header.js אשר מאפשר מנוע חיפוש בכל עמודי האתר. בנוסף הוא מאפשר לנווט בין תפריטי האתר כמו צפיה בעגלת הקניות, מועדפים, איזור אישי ועוד פעולות בחשבון.
4.	האתר שלנו מאפשר ללקוח לצפות במוצרים אותם האתר מציע ולחפש לפי מילת חיפוש או חצי ממנה. הלקוח יכול לשמור מוצרים שאהב ברשימת המועדפים ולהוסיף לעגלה לפי צבע ומידה. הלקוח כמובן יכול להתחרט ולהוריד מוצרים מהמועדפים ומעגלת הקניות. האתר מתעדכן בזמן אמת (כמו מילוי הלב באדם בהוספה למועדפים, או עדכון מספר הפריטים בעגלה באמצעות אייקון מספר בצבע אדום). יש ברשות האתר טופס להרשמה לאתר, יצירת קשר, והשארת פרטים. בכל אחד מהטפסים אשר הלקוח מתבקש להשאיר מידע אנו מבצעים ואלידציה למידע בזמן אמת (וידוא תקינות תווים ואורכם).
חשוב לציין כי יצרנו קובץ JS וCSS אשר משמשים את כל אחד מעמודי האתר. הם נועדו ליצור אחידות בנראות ובפונקציונליות של האתר.

מבנה הפרוקיט:
- front_page.htmlעמוד הבית הראשי עם קטגוריות המוצרים.
- about.htmlמידע על המותג.
-contact.html טופס יצירת קשר ללקוחות.
-cart.html עמוד המציג את עגלת הקניות, עם אפשרויות לעדכון ומחיקת פריטים.
- checkout.htmlעמוד סגירת חשבון לתהליך רכישה.
- favorites.htmlעמוד המועדפים, מציג פריטים שהמשתמש שמר.
-personalArea.html אזור אישי הכולל מידע על חשבון, היסטוריית הזמנות ומשובים.
-product.html עמוד פרטי מוצר, כולל בחירת מידה וצבע.
-denim.html, dresses.html, tops.html, new-arrivals.html עמודים המציגים קולקציות מוצרים לפי קטגוריות.
-search_results.html  תוצאות חיפוש דינמיות לפי שאילתת משתמש.
-header.html ,header.js כותרת כוללת ותסריט לניהול ניווט, חיפוש ותפריטים.
-styles.css  קובץ עיצוב מרכזי לעיצוב אחיד באתר.
פיצ'רים עיקריים
חיפוש דינמי: מציג תוצאות מיידיות מכל הקטגוריות.
מועדפים: ניהול פריטים שמורים לגישה מהירה.
עגלה חכמה: עדכון אוטומטי של כמויות וסכומים.
אזור אישי: פרטי חשבון, היסטוריית הזמנות ומשובים.
עיצוב רספונסיבי: מותאם לכל המכשירים
