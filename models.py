from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    # Store XP as JSON: {"path_name": xp_points}
    xp_data = db.Column(db.JSON, default=dict)
    recommended_path = db.Column(db.String(100), default="Undecided")
    last_explored = db.Column(db.String(100), default="None")
    # New fields for marketplace
    total_xp = db.Column(db.Integer, default=0)  # Total XP earned (lifetime)
    marketplace_xp = db.Column(db.Integer, default=0)  # XP available to spend
    owned_titles = db.Column(db.JSON, default=list)  # List of purchased titles
    weekly_quest_progress = db.Column(db.JSON, default=dict)  # Weekly quest completion tracking
    quiz_result = db.Column(db.String(100), default="Undecided")  # Recommended path from quiz
    # New fields for daily quest currency system
    total_coins = db.Column(db.Integer, default=0)  # Lifetime coins earned
    spendable_coins = db.Column(db.Integer, default=0)  # Coins available to spend


class WeeklyQuest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_start = db.Column(db.DateTime, default=lambda: datetime.utcnow())
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    xp_reward = db.Column(db.Integer, default=50)
    difficulty = db.Column(db.String(20), default="Medium")  # Easy, Medium, Hard
    icon = db.Column(db.String(50), default="fa-star")
    completed = db.Column(db.Boolean, default=False)

    def is_current_week(self):
        week_end = self.week_start + timedelta(days=7)
        return self.week_start <= datetime.utcnow() < week_end


class MarketplaceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300))
    xp_cost = db.Column(db.Integer, nullable=False)
    item_type = db.Column(db.String(50), default="title")  # title, badge, cosmetic
    icon = db.Column(db.String(50), default="fa-medal")
    color = db.Column(db.String(20), default="primary")
    rarity = db.Column(db.String(20), default="common")  # common, rare, epic, legendary
    track = db.Column(db.String(100), default="Global")  # Track-specific or Global


class DailyQuest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    icon = db.Column(db.String(50), default="fa-star")
    coins_reward = db.Column(db.Integer, default=10)
    difficulty = db.Column(db.String(20), default="Medium")  # Easy, Medium, Hard
    created_at = db.Column(db.DateTime, default=lambda: datetime.utcnow())
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)


class LeaderboardEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_xp = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer)
    weekly_xp = db.Column(db.Integer, default=0)
    week_start = db.Column(db.DateTime, default=lambda: datetime.utcnow())
    path = db.Column(db.String(100), default="Global")