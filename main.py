import random

class ShortVideo:
    """Represents a YouTube Short video with various metrics."""
    def __init__(self, title, views, watch_time_percent, likes, dislikes):
        self.title = title
        self.views = views
        self.watch_time_percent = watch_time_percent # % of video watched
        self.likes = likes
        self.dislikes = dislikes

    def __repr__(self):
        return (f"'{self.title}' | Views: {self.views} | Watch Time: {self.watch_time_percent:.1f}% | "
                f"Likes: {self.likes} | Dislikes: {self.dislikes}")

def calculate_naive_success(video):
    """
    AI's initial, naive understanding: More views = more success.
    This directly reflects the article's "Daha fazla izlenme = daha fazla başarı" (More views = more success) misconception.
    """
    return video.views

def calculate_sophisticated_success(video):
    """
    AI's more sophisticated understanding: Considers engagement beyond just views.
    This reflects the article's point about the algorithm being complex and personalized.
    """
    # A simplified model for "true" engagement/success
    # Views are important, but weighted by watch time and engagement (likes vs dislikes)
    engagement_score = (video.views * (video.watch_time_percent / 100.0)) + (video.likes - video.dislikes)
    return engagement_score

def main():
    # Simulate a few Shorts videos with different metric profiles
    videos = [
        ShortVideo("Cute Cat Compilation", 150000, 45.0, 2500, 50),
        ShortVideo("Quick Tech Tip", 80000, 75.0, 1800, 20),
        ShortVideo("Viral Dance Challenge", 200000, 20.0, 1000, 500), # High views, low engagement
        ShortVideo("Deep Dive Explanation", 30000, 90.0, 1200, 10),  # Low views, high engagement
        ShortVideo("Daily Vlog Snippet", 120000, 60.0, 2000, 100)
    ]

    print("--- Simulated YouTube Shorts Videos ---")
    for i, video in enumerate(videos):
        print(f"Video {i+1}: {video}")
    print("\n" + "="*40 + "\n")

    # --- AI's Naive Strategy ---
    print("--- AI's Naive Strategy: Optimize for Raw Views ---")
    best_video_naive = None
    max_naive_score = -1

    for video in videos:
        score = calculate_naive_success(video)
        print(f"'{video.title}' Naive Score (Views): {score}")
        if score > max_naive_score:
            max_naive_score = score
            best_video_naive = video

    print(f"\nNaive AI's choice for 'most successful' video: '{best_video_naive.title}' (Views: {best_video_naive.views})")
    # This choice might be the "Viral Dance Challenge" which has many views but low watch time/high dislikes.
    print("This strategy can be misleading, as high views alone don't guarantee true engagement or algorithmic favor.")
    print("This illustrates the article's core misconception: 'More views = more success' is often false.\n")
    print("="*40 + "\n")

    # --- AI's Sophisticated Strategy ---
    print("--- AI's Sophisticated Strategy: Optimize for Engagement (Views + Watch Time + Likes/Dislikes) ---")
    best_video_sophisticated = None
    max_sophisticated_score = -1

    for video in videos:
        score = calculate_sophisticated_success(video)
        print(f"'{video.title}' Sophisticated Score: {score:.2f}")
        if score > max_sophisticated_score:
            max_sophisticated_score = score
            best_video_sophisticated = video

    print(f"\nSophisticated AI's choice for 'most successful' video: '{best_video_sophisticated.title}' (Sophisticated Score: {max_sophisticated_score:.2f})")
    print("This strategy considers deeper engagement metrics, reflecting a more accurate understanding of algorithmic success.")
    print("It helps avoid the pitfalls of focusing solely on superficial metrics like raw view count.")
    print("\n--- Conclusion ---")
    print("The example shows how an AI (or content creator) can be misled by simple metrics.")
    print("Understanding the complex interplay of views, watch time, and engagement is crucial for true success on platforms like YouTube Shorts.")

if __name__ == "__main__":
    main()
